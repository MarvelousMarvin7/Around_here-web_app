#!/usr/bin/python3
""" holds class Service"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.orm import relationship


class Service(BaseModel, Base):
    """Representation of Product """
    if models.storage_t == 'db':
        __tablename__ = 'services'
        store_id = Column(String(60), ForeignKey('stores.id', ondelete='CASCADE'),
                          nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        service_price = Column(Float, nullable=False, default=0.00)
        image_url = Column(String(128), nullable=True)
        service_requests = relationship("ServiceRequest", backref="service")
    else:
        store_id = ""
        name = ""
        description = ""
        service_price = 0.00
        image_url = ""

    def __init__(self, *args, **kwargs):
        """initializes Service"""
        super().__init__(*args, **kwargs)
