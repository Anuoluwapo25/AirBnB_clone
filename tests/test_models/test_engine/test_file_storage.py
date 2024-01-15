import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        # Create some objects
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)

        # Check if all method returns the correct dictionary
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn(f"BaseModel.{obj1.id}", all_objects)
        self.assertIn(f"BaseModel.{obj2.id}", all_objects)

    def test_save_reload(self):
        # Create some objects
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)

        # Save and reload
        self.storage.save()
        self.storage.reload()

        # Check if the reloaded data is correct
        reloaded_objects = self.storage.all()
        self.assertEqual(len(reloaded_objects), 2)
        self.assertIn(f"BaseModel.{obj1.id}", reloaded_objects)
        self.assertIn(f"BaseModel.{obj2.id}", reloaded_objects)

    def test_reload_nonexistent_file(self):
        # Reload from a file that doesn't exist
        self.storage.reload()

        # Check if __objects is still empty
        reloaded_objects = self.storage.all()
        self.assertEqual(len(reloaded_objects), 0)


if __name__ == '__main__':
    unittest.main()

