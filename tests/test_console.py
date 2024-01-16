import unittest
from unittest.mock import patch
from io import StringIO
from your_module_name import HBNBCommand  # Replace 'your_module_name' with the actual name of your module

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        with patch('builtins.input', return_value="create BaseModel") as mock_input:
            self.hbnb_command.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class name missing **", output)

        with patch('builtins.input', return_value="create MyModel") as mock_input:
            self.hbnb_command.onecmd("create MyModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual("** class doesn't exist **", output)

        with patch('builtins.input', return_value="create BaseModel") as mock_input:
            with patch('models.storage.save') as mock_save:
                self.hbnb_command.onecmd("create BaseModel")
                output = mock_stdout.getvalue().strip()
                self.assertTrue(output)
                self.assertTrue(mock_save.called)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        with patch('builtins.input', return_value="show") as mock_input:
            self.hbnb_command.onecmd("show")
            output = mock_stdout.getvalue().strip()
            self.assertEqual('** class name missing **', output)

        with patch('builtins.input', return_value="show BaseModel") as mock_input:
            self.hbnb_command.onecmd("show BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual('** instance id missing **', output)

        with patch('builtins.input', return_value="show BaseModel 1234") as mock_input:
            with patch('models.storage.save') as mock_save:
                self.hbnb_command.onecmd("show BaseModel 1234")
                output = mock_stdout.getvalue().strip()
                self.assertEqual('** no instance found **', output)

if __name__ == '__main__':
    unittest.main()

