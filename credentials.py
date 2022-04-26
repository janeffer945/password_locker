class Credentials:
    """
    Class that generates new instances of credentials.
    """

    accounts_list = [] 
    
    def __init__(self, acc_name, user_name, user_password):
        '''
        method that defines variables to be used
        '''

        self.acc_name = acc_name
        self.user_name = user_name
        self.user_password = user_password

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the accounts_list
        '''
        return cls.accounts_list
    
        
    @classmethod
    def save_credential(self):

        '''
        save_credential method saves account objects into accounts_list
        '''

        Credentials.accounts_list.append(self)
    @classmethod
    def find_credential(cls,acc_name):
       '''
        find_credential method finds account 
        '''
       for credential in cls.accounts_list:
            if credential.acc_name==acc_name:
                return credential
    @classmethod
    def delete_account(self):
        '''
        method that deletes a saved account from the account list
        '''
        Credentials.accounts_list.remove(self)   