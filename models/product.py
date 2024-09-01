#!/usr/bin/python
""" holds class Product"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """Representation of Product """
    if models.storage_t == 'db':
        __tablename__ = 'products'
        store_id = Column(String(60), ForeignKey('stores.id', ondelete='CASCADE'),
                          nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        price = Column(Integer, nullable=False, default=0)
        reviews = relationship("Review", backref="product")
        order_items = relationship("OrderItem", backref="product", cascade="all, delete")
    else:
        store_id = ""
        name = ""
        description = ""
        price = 0

    def __init__(self, *args, **kwargs):
        """initializes Product"""
        super().__init__(*args, **kwargs)
