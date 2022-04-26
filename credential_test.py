import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase) :
    '''
    Test class that defines test cases for the Credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Credentials("Facebook","janeffer", "0746397945") 
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.acc_name, "Facebook")
        self.assertEqual(self.new_account.user_name, "janeffer")
        self.assertEqual(self.new_account.user_password,"0746397994")
        
        
        
       
       