#!/usr/bin/python3
"""This module defines a class User."""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes."""

    __tablename = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
