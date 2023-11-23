import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_missing_class_name(self, mock_stdout):
        self.console.do_create("")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_invalid_class_name(self, mock_stdout):
        self.console.do_create("InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_no_parameters(self, mock_stdout):
        self.console.do_create("BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("Missing parameter"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_valid_parameters(self, mock_stdout):
        self.console.do_create("BaseModel name='test' age=25")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("Generated object ID:"))

if __name__ == '__main__':
    unittest.main()