# CONTINUATION from the unit test file unitTestUsingunittestModule.py
import unittest
from unittest.mock import patch #This will allow us to mock during test and restore after test is run
from employee import Employee #Import the class Employee form the employee module that we created

#Usually you should try to make your programming DRY (Don't Repeat Yourself)
#If you notice below, we are defining two employees in each of the tests below.
#There should be a better way to do this???
#That is what setup and teardowns methods are used for. Look at the first and second functions after the
#class definition below
#Tests don't run in order and you will need to keep all of your tests isolated and not linked

#You can use the SetUp class and TearDown class to run Setup only once during the beginning and Tear Down class only once during the ending of all tests
# Look below at the example

#### LOOK AT THE BOTTOM HERE FOR MOCKING EXAMPLE ####
# Mocking is used in situations where the fuctions being tested could fail due to outside dependency
# For example, if the function uses data from an external website and if the website is down, we do not want
# our tests to fail.
# LOOK AT EMPLOYEE CLASS FOR THE EXAMPLE OF A FUNCTION USED TO MOCK
# ALSO LOOK AT THE IMPORTS TO FIND A MOCKING UNITTEST IMPORT

class TestEmployee(unittest.TestCase):

    ######SETUP AND TEARDOWN CLASSES######
    @classmethod #Class methods will run similar per class
    def setUpClass(cls):
        print('setupClass')
    
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self): #setup method will run before every test
        self.emp_1 = Employee('Caramel', 'Madadi', 100000)
        self.emp_2 = Employee('Urvi', 'Madadi', 150000)

    def tearDown(self): #teardown method will run after every test
        pass

    def test_email(self):
        # emp_1 = Employee('Caramel', 'Madadi', 50000)
        # emp_2 = Employee('Urvi', 'Madadi', 60000)

        self.assertEqual(self.emp_1.email, 'Caramel.Madadi@email.com')
        self.assertEqual(self.emp_2.email, 'Urvi.Madadi@email.com')

        self.emp_1.first = 'Caru'
        self.emp_2.first = 'Cutiepie'

        self.assertEqual(self.emp_1.email, 'Caru.Madadi@email.com')
        self.assertEqual(self.emp_2.email, 'Cutiepie.Madadi@email.com')
    
    def test_fullname(self):
        # emp_1 = Employee('Caramel', 'Madadi', 80000)
        # emp_2 = Employee('Urvi', 'Madadi', 100000)

        self.assertEqual(self.emp_1.fullname, 'Caramel Madadi')
        self.assertEqual(self.emp_2.fullname, 'Urvi Madadi')

        self.emp_1.first = 'Caru'
        self.emp_2.first = 'Cutiepie'

        self.assertEqual(self.emp_1.fullname, 'Caru Madadi')
        self.assertEqual(self.emp_2.fullname, 'Cutiepie Madadi')
    
    def test_apply_raise(self):
        # emp_1 = Employee('Caramel', 'Madadi', 100000)
        # emp_2 = Employee('Urvi', 'Madadi', 150000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 105000)
        self.assertEqual(self.emp_2.pay, 157500)
    
    # Example of mocking
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get: #We are patching here the request.get from employee module with mocked_get
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Madadi/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Madadi/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()