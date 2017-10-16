from HW4_Task1_Emp import Employee

class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []

    def add_skills(self, skill_name):
        self.skills.append(skill_name)

    def level_skills(self, experience):
        if 0 < experience < 3:
            return 'Junior'
        elif 3 <= experience < 6:
            return 'Middle'
        elif experience >= 6:
            return 'Senior'

if __name__ == "__main__":
    emp1 = ITEmployee('Nataliia Tiutiunnyk', 'QA', 26000)
    emp1.add_skills('SQL')
    print(emp1.skills[0])
    print(emp1.level_skills(5))

