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

