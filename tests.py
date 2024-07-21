import unittest
from hello import say_hi

class test_function(unittest.TestCase):
    def test_result(self):
        assert say_hi() == 'hello, world'