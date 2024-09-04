#!/usr/bin/python3
""" holds class ServiceRequest"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, DateTime, ForeignKey, String, Enum


class ServiceRequest(BaseModel, Base):
    """Representation of ServiceRequest """
    if models.storage_t == 'db':
        __tablename__ = 'service_requests'
        service_id = Column(String(60), ForeignKey('services.id'),
                            nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        address = Column(String(128), nullable=True)
        schedule_time = Column(DateTime, nullable=False)
        status = Column(Enum('pending', 'confirmed', 'completed',
                              'cancelled'), nullable=False, default='pending')
        notes = Column(String(1024), nullable=True)
    else:
        service_id = ""
        user_id = ""
        schedule_time = ""
        status = "pending"
        notes = ""

    def __init__(self, *args, **kwargs):
        """initializes ServiceRequest"""
        super().__init__(*args, **kwargs)
