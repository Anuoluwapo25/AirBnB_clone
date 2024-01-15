#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class test_base_model(unittest.TestCase):
    def test_id(self):
        self.assertEqual(BaseModel.id, str)
    
        
        

    