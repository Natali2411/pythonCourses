import unittest
from HW3_Task5 import is_year_leap

class Test_Is_year_leap(unittest.TestCase):

    def test_true(self):
        self.assertEqual(is_year_leap(1992), 'True')
        self.assertEqual(is_year_leap(2003), 'False')
        self.assertNotEquals(is_year_leap(2004), 'False')

    def test_less_more(self):
        self.assertGreater((is_year_leap(2016)), 'False')
        self.assertLess(is_year_leap(2015), 'True')