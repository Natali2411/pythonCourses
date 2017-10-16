import unittest
import re
from HW3_Task5 import is_triangle

class Test_Is_triangle(unittest.TestCase):
    sides1 = [[0,1,4], [3,6,7], [-4,-6,8], ['gfj',7,'8']]
    sides2 = [[5,6,4], [3,6,7], [4,6,8]]
    def test_type(self):
        for i in range(len(self.sides1)):
            for j in range(len(self.sides1[i])):
                self.assertRegex(str(self.sides1[i][j]), re.compile(r'\w'))
                self.assertRegex(str(self.sides1[i][j]), re.compile(r'\d'))

    def test_equal(self):
        for i in range(len(self.sides2)):
            self.assertEqual(is_triangle(self.sides2[i][0], self.sides2[i][1], self.sides2[i][2]), 'True')
            self.assertNotEqual(is_triangle(self.sides2[i][0], self.sides2[i][1], self.sides2[i][2]), 'False')

    def test_assert_error(self):
        for i in range(len(self.sides1)):
            with self.assertRaises(TypeError):
                is_triangle(self.sides1[i][0], self.sides1[i][1], self.sides1[i][2])