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
