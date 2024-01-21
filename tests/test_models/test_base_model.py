#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class test_base_model(unittest.TestCase):
    def test_id(self):
        self.assertEqual(type(BaseModel.id), str)
    def test_created_at(self):
        self.assertEquals(type(BaseModel.created_at), datetime)
    def test_updated(self):
        self.assertEquals(type(BaseModel.updated_at), datetime)
    def test_dics(self):
        self.assertEquals(type(BaseModel.to_dict()), dict)
if __name__ == '__main__':
    unittest.loop
