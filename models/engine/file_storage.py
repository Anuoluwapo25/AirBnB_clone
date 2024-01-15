#!/usr/bin/python3
"""Module for file storage"""
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
        self.__objects[keyo] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        with open(self.__file_path, "w") as file:
            json.dump({key: obj.to_dict() for key,
                obj in self.__objects.items()}, file)
        
    def reload(cls):
        """Deserializes the JSON file to __objects"""

        try:
            with open(cls.__file_path, 'r', encoding='utf-8') as file:
                cls.__objects = json.load(file)

        except FileNotFoundError:
            pass
