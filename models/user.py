#!/usr/bin/python3
"""class User that inherits from BaseModel"""
from models.base_models import BaseModel


class User(BaseModel):
    """Defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
