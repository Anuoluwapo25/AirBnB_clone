#!/usr/bin/python3
"""
module that inherit BaseModel
"""
 from model.base_model import BaseModel

class User(BaseModel):
    """
    properties from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
