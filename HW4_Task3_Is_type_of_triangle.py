import unittest
from HW3_Task6 import is_type_of_triangle

class Test_Is_type_of_triangle(unittest.TestCase):
    sides1 = [[2,2,2], [3,5,5], [0,1,6], [6,7,9]]
    def test_reg_match(self):
        self.assertRegex(is_type_of_triangle(self.sides1[0][0], self.sides1[0][1], self.sides1[0][2]), 'Equilateral triangle')
        self.assertRegex(is_type_of_triangle(self.sides1[1][0], self.sides1[1][1], self.sides1[1][2]), 'Isosceles triangle')
        self.assertRegex(is_type_of_triangle(self.sides1[2][0], self.sides1[2][1], self.sides1[2][2]), 'Not a triangle')
        self.assertRegex(is_type_of_triangle(self.sides1[3][0], self.sides1[3][1], self.sides1[3][2]), 'Versatile triangle')