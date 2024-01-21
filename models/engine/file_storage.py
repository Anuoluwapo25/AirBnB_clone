#!/usr/bin/python3
"""Module for file storage"""
import models
import json
import os


class FileStorage():
    """_summary_

    Returns:
        _type_: _description_
    """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """returns the d__objects"""
        return self.__objects
    

    def new(self, obj):
        """sets in __objects the obj with key"""
        keyo = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[keyo] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        with open(self.__file_path, "w") as file:
            json.dump({key: obj.to_dict() for key,
                obj in self.__objects.items()}, file)

        
    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as file:
                    obj_en = json.load(file)
                for key, value in obj_en.items():
                    class_name = value.get('__class__')
                    if class_name in class_list:
                        new_inst = class_list[class_name](**value)
                        self.__objects[key] = new_inst
            except FileNotFoundError:
                pass
        else:
            pass

