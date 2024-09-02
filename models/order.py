#!/usr/bin/python
""" holds class Order"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String, Integer, Enum
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """Representation of Order """
    if models.storage_t == 'db':
        __tablename__ = 'orders'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        address = Column(String(128), nullable=False)
        payment_method = Column(Enum('cash', 'mobile_money'), nullable=False)
        status = Column(Enum('pending', 'processing', 'shipped', 'delivered',
                             'cancelled'), nullable=False, default='pending')
        order_items = relationship("OrderItem", backref="order")
    else:
        user_id = ""
        address = ""
        payment_method = "mobile_money"
        status = "pending"

    def __init__(self, *args, **kwargs):
        """initializes Order"""
        super().__init__(*args, **kwargs)
