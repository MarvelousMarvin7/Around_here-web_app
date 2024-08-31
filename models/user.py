#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import BOOLEAN, Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False, unique=True)
        password = Column(String(128), nullable=False)
        user_name = Column(String(128), nullable=False)
        website = Column(String(128), nullable=True)
        is_store_owner = Column(BOOLEAN, nullable=False, default=False)
        stores = relationship("Store", backref="user")
        orders = relationship("Order", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        user_name = ""
        website = ""
        is_store_owner = False

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)