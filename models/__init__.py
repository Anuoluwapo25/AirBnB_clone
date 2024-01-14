#!/usr/bin/python3
"""
modulu which create insatnce of FileStorage class
"""
import json
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
