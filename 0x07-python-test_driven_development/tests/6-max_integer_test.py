#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for doc string"""
    def test_doc_string(self):
        docs = __import__('6-max_integer').__doc__
        self.assertTrue(len(docs) > 1)
        self.assertTrue(len(max_integer.__doc__) > 1)
        
    """When no parameteris passed to the function"""
    def test_no_argument(self):
        self.assertIsNone(max_integer(), "No parameter was passed to the function :(")

    """When the function is given the correct values"""
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1,3,4,10]), 10)
        self.assertEqual(max_integer([1,3,10.3,10]), 10.3)
    
    """Raising a type error if value is not a float or integer"""
    def test_type(self):
        self.assertRaises(TypeError, max_integer, [1, "1", 20])
        self.assertRaises(TypeError, max_integer, ["one", False, 5])
        self.assertRaises(TypeError, max_integer, [2 + 5j, 20, 1])
