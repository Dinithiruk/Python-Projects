from Employee import Employee

class Manager(Employee):
    def __init__(self, firstname, lastname, salary, department):
        super().__init__(firstname, lastname, salary)
        self.department = department

    def self_introduce(self):
        print("Hello, I'm {} {}. I manage the {} department. My salary is ${} per year.".format(self.firstname, self.lastname, self.department, self.salary))

    def calculate_monthly_pay(self):
        monthly_pay = self.salary / 12
        print("Monthly pay for {} {} (Manager): ${:.2f}".format(self.firstname, self.lastname, monthly_pay))

    def assign_bonus(self, employee, bonus):
        employee.salary += bonus
        print("Bonus of ${} assigned to {} {}".format(bonus, employee.firstname, employee.lastname))

#instances
if __name__ == "__main__":
    employee1 = Employee("Tom","David",3000)
    employee2= Employee ("Johanson","Mark",2400)
    employee3 = Employee("Sally","Harthay",5400)

    manager1 = Manager("Gigi","Hadid",5000,"Sales")
    manager2 = Manager("Kendall", "Jenner",6000,"Finance")
    manager3 = Manager("Hailey","Bieber",2300,"HR")

print("--------------------- Employee details ------------------ \n")
#calling the methods
employee1.self_introduce()
employee1.calculate_monthly_salary()
print("\n")

employee2.self_introduce()
employee2.calculate_monthly_salary()
print("\n")

employee3.self_introduce()
employee3.calculate_monthly_salary()
print("\n")

print("------------------ Managers details ---------------- \n")
manager1.self_introduce()
manager1.calculate_monthly_salary()
print("\n")

manager2.self_introduce()
manager2.calculate_monthly_salary()
print("\n")

manager3.self_introduce()
manager3.calculate_monthly_salary()
print("\n")

#allowing the bonus for the 3rd employee
manager1.assign_bonus(employee3,4000)
print("\n")

employee3.self_introduce()
employee3.calculate_monthly_pay()
print("\n")