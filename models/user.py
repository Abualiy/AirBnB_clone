#!/usr/bin/python3
"""user Calss module"""
from models.base_model import BaseModel


class User(BaseModel):
    """user object managing class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
