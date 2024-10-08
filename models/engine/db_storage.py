#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.base_model import Base, BaseModel
from models.service_request import ServiceRequest
from models.user import User
from models.store import Store
from models.service import Service
from models.order import Order
from models.product import Product
from models.order_item import OrderItem
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {'BaseModel': BaseModel, 'User': User, 'Store': Store, 'Service': Service,
            'ServiceRequest': ServiceRequest, 'Order': Order, 'OrderItem': OrderItem,
              'Product': Product, 'Review': Review}


class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        ARH_MYSQL_USER = getenv('ARH_MYSQL_USER')
        ARH_MYSQL_PWD = getenv('ARH_MYSQL_PWD')
        ARH_MYSQL_HOST = getenv('ARH_MYSQL_HOST')
        ARH_MYSQL_DB = getenv('ARH_MYSQL_DB')
        ARH_ENV = getenv('ARH_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(ARH_MYSQL_USER,
                                             ARH_MYSQL_PWD,
                                             ARH_MYSQL_HOST,
                                             ARH_MYSQL_DB))
        if ARH_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Returns the object based on the class and its ID"""
        if cls and id:
            return self.__session.query(cls).filter_by(id=id).first()
        return None

    def count(self, cls=None):
        """Returns the number of objects in storage matching the given class"""
        if cls:
            return self.__session.query(cls).count()
        else:
            count = 0
            for cls_name in classes.values():
                count += self.__session.query(cls_name).count()
            return count