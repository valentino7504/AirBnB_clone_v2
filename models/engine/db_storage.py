#!/usr/bin/python3
"""This module defines the DBStorage class to manage database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """This class manages the storage of the hbnb models in MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialiser for the hbnb Database storage"""
        _username = getenv("HBNB_MYSQL_USER")
        _password = getenv("HBNB_MYSQL_PWD")
        _database = getenv("HBNB_MYSQL_DB")
        _host = getenv("HBNB_MYSQL_HOST")
        _mode = getenv("HBNB_ENV")
        _connection_string = f"mysql+mysqldb://{_username}:{_password}@"
        _connection_string += f"{_host}:3306/{_database}"
        self.__engine = create_engine(_connection_string, pool_pre_ping=True)
        if _mode == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all the object specified by cls"""
        from models.state import State
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        obj = []
        if cls:
            obj.extend(self.__session.query(cls).all())
        else:
            obj.extend(self.__session.query(State).all() +
                       self.__session.query(City).all() +
                       self.__session.query(User).all() +
                       self.__session.query(Review).all() +
                       self.__session.query(Amenity).all() +
                       self.__session.query(Place).all())
        return {f"{row.__class__.__name__}.{row.id}": row for row in obj}

    def new(self, obj):
        """Adds a new obj to the current Session object"""
        self.__session.add(obj)

    def save(self):
        """commits all the performed operation so far to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from the session"""
        self.__session.delete(obj)

    def reload(self):
        """connects the engine to the database"""
        from models.state import State
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
