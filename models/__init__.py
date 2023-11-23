#!/usr/bin/python3
"""This module instantiates an object of class FileStorage."""
from models.engine.file_storage import FileStorage
from os import environ as require
from models.engine.db_storage import DBStorage


if require.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
