
import requests

#### LOOK AT THE BOTTOM OF EMPLOYEE CLASS FOR MOCKING EXAMPLE ####
# Mocking is used in situations where the fuctions being tested could fail due to outside dependency
# For example, if the function uses data from an external website and if the website is down, we do not want
# our tests to fail.
# LOOK AT EMPLOYEE CLASS FOR THE EXAMPLE

class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#Sample method used to explain mocking

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
        
    