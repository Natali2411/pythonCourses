class Employee:
    def __init__(self, full_name, position, salary):
        self.full_name = full_name
        self.position = position
        self.salary = salary

    def emp_1st_name(self):
        first_name = self.full_name.split(' ')
        return first_name[0]

    def emp_2nd_name(self):
        second_name = self.full_name.split(' ')
        return second_name[1]

    def income(self, count_months):
        return self.salary * count_months

if __name__ == "__main__":
    emp_name = Employee('Nataliia Tiutiunnyk', 'QA', 26000)
    print(emp_name.emp_1st_name())
    print(emp_name.emp_2nd_name())
    print(emp_name.income(5))