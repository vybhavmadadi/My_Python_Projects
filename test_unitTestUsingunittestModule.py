#Unit tests for the file named unitTestUsingunittestModule.py
import unittest #Module for unit testing
import unitTestUsingunittestModule #Import our module that we want to test

# Create test cases to test our functions from the unitTestUsingunittestModule file

class TestCalc(unittest.TestCase): #TestCalc is your custom variable inheriting the unittest.TestCase giving us access to lot of different testing capability from that class

    def test_add(self): #This test function will need to start with 'test_' if not it will not be considered for test
                        #Like any method in a class, this takes 'self' as the first argument
# All asserts that possible can be found here 'https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
        # result = unitTestUsingunittestModule.add(10, 5)
        # self.assertEqual(result, 15) #Using assert to check if the result is what is expected of the result

#Defining the above test in a better way and adding more asserts, however as they all are in one test
#the output will only say as one test was run.
        self.assertEqual(unitTestUsingunittestModule.add(10, 5), 15)
        self.assertEqual(unitTestUsingunittestModule.add(-1, 1), 0)
        self.assertEqual(unitTestUsingunittestModule.add(-1, -1), -2)

# To run this test, open terminal and navigate to the path of the test and run this test using
# python -m unittest <unit test file name>
# The result will show how many tests were run and the amount of time it took and the result as OK or F (FAIL) and what test failed and for what assertion.

# If you want to run the test without using the python -m unitest method, you can define the following
# to directly run this test by calling the file using python <file name> or directly in this editor

#Adding rest of our tests
    def test_sub(self):
        self.assertEqual(unitTestUsingunittestModule.subtract(10, 5), 5)
        self.assertEqual(unitTestUsingunittestModule.subtract(-1, 1), -2)
        self.assertEqual(unitTestUsingunittestModule.subtract(-1, -1), 0)
    
    def test_mul(self):
        self.assertEqual(unitTestUsingunittestModule.multiply(10, 5), 50)
        self.assertEqual(unitTestUsingunittestModule.multiply(-1, 1), -1)
        self.assertEqual(unitTestUsingunittestModule.multiply(-1, -1), 1)
    
    def test_div(self):
        self.assertEqual(unitTestUsingunittestModule.divide(10, 5), 2)
        self.assertEqual(unitTestUsingunittestModule.divide(-1, 1), -1)
        self.assertEqual(unitTestUsingunittestModule.divide(-1, -1), 1)
# To check exceptions, you have use assertRaises and then define the attributes by commas instead of paranthesis
        self.assertRaises(ValueError, unitTestUsingunittestModule.divide, 10, 0)
# But a better way to test exeptions is using context manager, like this
        with self.assertRaises(ValueError):
            unitTestUsingunittestModule.divide(10, 0)

if __name__ == '__main__':
    unittest.main()