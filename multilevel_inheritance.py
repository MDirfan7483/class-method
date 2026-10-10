class Employee:
    a = 1
class programmer(Employee):
    b = 0

class manager(programmer):
    c = 3

o = Employee()
print(o.a)
# print(o.b) #error

o = programmer()
print(o.a, o.b,)

o = manager()
print(o.a, o.b, o.c)