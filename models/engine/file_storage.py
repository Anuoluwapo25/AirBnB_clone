#!/usr/bin/python3
"""Module for file storage"""
from model.base_model import BaseModel
import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the d__objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        keyo = f"{obj.__class__.__name__}.{obj.id}"
        self.__object[key] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        encod_obj = {}
        for key, obj in self.__objects.items():
            encod_obj[key] = obj.to_dic()

        with open(self.__file_path, "w") as file:
            json.dump(encod_obj, file)
    def reload(self):
        """Deserializes th JSON file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    decodeobj = json.load(file)
                    for key, value in decodeobj.items():
                        class_name, obj_id = key.split('.')
                        class_type = eval(class_name)
                        obj_instance = class_type(**obj_dict)
                        self.__objects[key] = obj_instance

                except json.JSONDecodeError:
                    pass

