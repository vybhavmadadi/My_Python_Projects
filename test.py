import sys

print(sys.executable)
print(sys.version)


class Employee:
    """A sample Employee class"""

    def ___init___(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".formt(self.first, self.last)


emp_1 = Employee("John", "Smith")

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
