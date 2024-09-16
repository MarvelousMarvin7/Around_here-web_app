#!/usr/bin/python3
""" holds class User"""
import bcrypt
import models
from models.base_model import BaseModel, Base
from sqlalchemy import BOOLEAN, Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        user_name = Column(String(128), nullable=False)
        image_url = Column(String(128), nullable=True)
        is_store_owner = Column(BOOLEAN, nullable=True, default=False)
        stores = relationship("Store", backref="user")
        orders = relationship("Order", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        user_name = ""
        image_url =""
        is_store_owner = False

    def __init__(self, *args, **kwargs):
        """initializes user"""
        if 'password' in kwargs:
            kwargs['password'] = self.hash_password(kwargs['password'])
        super().__init__(*args, **kwargs)

    def hash_password(self, password):
        """hashes password"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def is_valid_password(self, password):
        """checks if password is valid"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

