import re
import unittest
from HW4_Task1_ITEmp import ITEmployee

class test_ITEmployee(unittest.TestCase, ITEmployee):

    def test_init(self):
        ITEmployee.__init__(self, 'Nataliia Tiutiunnyk', 'QA', 25000)
        self.assertTrue(self.full_name, self.position)
        self.assertTrue(self.salary)
        #print(self.skills)
    def test_add_skills(self):
        ITEmployee.add_skills(self, 'SQL')
        ITEmployee.add_skills(self, 'HTML')
        self.assertEqual(len(self.skills),2)
        for i in range(len(self.skills)):
            self.assertRegex(self.skills[0],re.compile(r'SQL|HTML'))

    def test_level_skills(self):
        for i in range(0, 10):
            if 0 < i < 3:
                self.assertEqual(ITEmployee.level_skills(self,i), 'Junior')
            elif 3 <= i < 6:
                self.assertEqual(ITEmployee.level_skills(self,i), 'Middle')
            elif 6 <= i <= 10:
                self.assertEqual(ITEmployee.level_skills(self,i), 'Senior')



