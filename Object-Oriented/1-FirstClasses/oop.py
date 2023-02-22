
# class Employee:

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)

# class Employee:
#     pass 

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# instance variables contain data unique to each instance 

class Employee:

    def __init__(self, first, last, pay):
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        if not (first and bool(first.strip())):
            raise ValueError("first can't be empty or null")
        self.first = first

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_1 = Employee('', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.fullname()) # Corey Schafer
print(emp_2.fullname()) # Test Employee


name = "alex" # True
# name = "" # False
# if after stripping name, name is an empty string = False, raise value error
q = bool(name.strip())
print("Q: ",q)