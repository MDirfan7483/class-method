class Employee:
    def __init__(self):
        print("Constructor of employee")
    a = 1
class programmer(Employee):
    def __init__(self):
        print("Constructor of programmer")
    b = 0

class manager(programmer):
    def __init__(self):
        print("Constructor of manager")
        super().__init__()
    c = 3

o = Employee()
# print(o.a)
# print(o.b) #error

# o = programmer()
# print(o.a, o.b,)

o = manager()
print(o.a, o.b, o.c)