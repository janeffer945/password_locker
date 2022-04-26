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
    def test_display_all_accounts(self):
        '''
        method that returns a list of saved accounts
        '''

        self.assertEqual(Credentials.display_accounts(), Credentials.accounts_list)


    def test_save_all_accounts(self):
        '''
        method that saves a new account
        '''
        self.new_account.save_credential()  
        test_account = Credentials("Facebook","janeffer","0746397994") #new account
        test_account.save_credential()
        self.assertEqual(len(Credentials.accounts_list), 3)


    def test_delete_account(self):
        '''
        a test to know if we can delete an account.
        '''
        self.new_account.save_credential()
        test_account = Credentials("Facebook","janeffer", "0746397994")
         

       
       