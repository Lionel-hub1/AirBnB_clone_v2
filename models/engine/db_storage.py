#!/usr/bin/python3
from os import environ
from sqlalchemy import (create_engine)


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
                '{}://{}:{}@{}'.format(
                    environ.get(HBNB_MYSQL_DB),
                    environ.get(HBNB_MYSQL_USER),
                    environ.get(HBNB_MYSQL_PWD),
                    environ.get(HBNB_MYSQL_HOST)
                    ),
                pool_pre_ping=True)
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        ))
        self.__session = Session()

        def all(self, cls=None):
            """Query objects from the current database session."""
        from models import classes  # Import all classes before creating tables
        result = {}

        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for class_name in classes:
                objects.extend(self.__session.query(classes[class_name]).all())

        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            result[key] = obj

        return result

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session if obj is not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and the current session."""
        from models import classes
        Base.metadata.create_all(self.__engine)

    def close(self):
        """Close the session."""
        self.__session.remove()
