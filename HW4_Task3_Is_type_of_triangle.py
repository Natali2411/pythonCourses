import unittest
import re
from HW3_Task6 import is_type_of_triangle

class test_is_type_of_triangle(unittest.TestCase):
    sides1 = [[2,2,2], [3,5,5], [0,1,6], [6,7,9]]
    sides2 = [[1,5,6],['asd',5,'7'],['/',5,'!_?']]
    def test_reg_match(self):
        self.assertRegex(is_type_of_triangle(self.sides1[0][0], self.sides1[0][1], self.sides1[0][2]), 'Equilateral triangle')
        self.assertRegex(is_type_of_triangle(self.sides1[1][0], self.sides1[1][1], self.sides1[1][2]), 'Isosceles triangle')
        self.assertRegex(is_type_of_triangle(self.sides1[2][0], self.sides1[2][1], self.sides1[2][2]), 'Not a triangle')
        self.assertRegex(is_type_of_triangle(self.sides1[3][0], self.sides1[3][1], self.sides1[3][2]), 'Versatile triangle')

    def test_not_reg(self):
        for i in range(len(self.sides2)):
            self.assertNotRegex(is_type_of_triangle(str(self.sides2[i][0]),str(self.sides2[i][1]),str(self.sides2[i][2])), re.compile(r'Equilateral | Isosceles | Not'))

    def test_error(self):
        for i in range(len(self.sides2)):
            for j in range(len(self.sides2[i])):
                self.assertRegex(str(self.sides2[i][j]), re.compile(r'\d'))

