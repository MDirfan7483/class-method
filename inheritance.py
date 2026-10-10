class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class progemmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")


#     def showlanguge(self):
#         print(f"The name is {self.name} and he is good in language {self.language}")
class Programmer(Employee):
    company = "ITC Infotech"
    def showlanguge(self):
        print(f"The name is {self.name} and the salary is {self.salary} he is good in language {self.language}")


a = Employee()
b = Programmer()
print(a.company, b.company)      