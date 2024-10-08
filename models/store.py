#!/usr/bin/python3
"""holds class Store"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Enum, Float, String, Time, ForeignKey
from sqlalchemy.orm import relationship


class Store(BaseModel, Base):
    """Representation of Store"""
    if models.storage_t == 'db':
        __tablename__ = 'stores'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        location = Column(String(128), nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        description = Column(String(1024), nullable=True)
        image_url = Column(String(128), nullable=True)
        contact = Column(String(13), nullable=False)
        opening_time = Column(Time, nullable=False, default="00:00")
        closing_time = Column(Time, nullable=False, default="23:59")
        reviews = relationship("Review", backref="store")
        products = relationship("Product", backref="store",
                                cascade="all, delete")
        services = relationship("Service", backref="store",
                                cascade="all, delete")
    else:
        user_id = ""
        name = ""
        location = ""
        latitude = 0.0
        longitude = 0.0
        description = ""
        image_url = ""
        contact = ""
        opening_time = "00:00"
        closing_time = "23:59"

    def __init__(self, *args, **kwargs):
        """initializes Store"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.store_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def products(self):
            """getter attribute returns the list of Product instances"""
            from models.product import Product
            product_list = []
            all_products = models.storage.all(Product)
            for product in all_products.values():
                if product.store_id == self.id:
                    product_list.append(product)
            return product_list
