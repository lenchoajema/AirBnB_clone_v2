#!/usr/bin/python3
'''DBStorage engine'''

import MySQLdb
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os


class DBStorage:
    '''class for DBStorage'''
    __engine = None
    __session = None

    def __init__(self):
        '''Initializes DBStorage'''
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
            # Drop all tables for testing purposes

    def all(self, cls=None):
        '''Query all objects on current database session'''
        all_dict = {}
        if cls:
            result = self.__session.query(eval(cls)).all()
        else:
            result = []
            _list = ['User', 'State', 'City', 'Review', 'Place', 'Amenity']
            for i in _list:
                y = self.__session.query(eval(i))
                for j in y:
                    result.append(j)

        for obj in result:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            # key convention - <class-name>.<object-id>
            all_dict[key] = obj
        return all_dict

    def new(self, obj):
        '''Adds object to current database session'''
        self.__session.add(obj)

    def save(self):
        '''Commits all changes of current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Deletes obj from current database session'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''Creates current db session from engine and all tables in db'''
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Call remove method to close SQLAlchemy"""
        self.__session.close()
