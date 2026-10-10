class Employee:
    company = "ITC"
    name = "Defalut name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class coder:
    Language = "Python"
    def printlanguage(self):
        print(f"Out of all language here is your language: {self.Language}")
     
class Programmer(Employee, coder):
    company = "ITC Infotech"
    def showlanguge(self):
        print(f"The name is {self.company} and he is good with language {self.Language}")

a = Employee()
b = Programmer()

b.show() 
b.printlanguage()
b.showlanguge()  