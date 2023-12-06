class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def self_introduce(self):
        print("Hello, I'm {} {} and currently I'm earning a monthly salary of {} ".format(self.firstname,self.lastname,self.salary))

    def calculate_monthly_salary(self):
        monthly_pay = self.salary/12
        print("Name : {} {} \nMonthly salary : {} ".format(self.firstname,self.lastname,monthly_pay))





