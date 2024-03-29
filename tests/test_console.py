#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from console import HBNBCommand
import unittest


class test_Console(test_basemodel):
    """ Unittests for console """

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    def test_emptyline(self, mock_stdout):
        self.console.onecmd('')
        self.assertEqual(mock_stdout.getvalue(), '')

    def test_do_quit(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.onecmd('quit')
        self.assertEqual(mock_stdout.getvalue(), '')


if __name__ == '__main__':
    unittest.main()
