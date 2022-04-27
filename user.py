
class Users:
    """class that generates new instances of users
    """
    users_list = []
    
    def  __init__(self,username,login_password):
        """
         method that helps us define properties for our object
        Args:
            username :New username
            login_password:New user password
        """
        self.username = username
        self.login_password = login_password
             
    def  add_user(self):
        """
        add user details method saves user objects
        """
        Users.users_list.append(self)
    
    def  delete_user(self):
        """
        method removes user details
        """  
        Users.users_list.remove(self) 
        
    @classmethod
    def  find_by_username(cls,username):
        """
        authenticate user 

        Args:
            username:name used by user to login in
        """
        for user in Users.users_list:
            if user.username == username:
                return user
            
    @classmethod
    def  user_exists(cls,username,login_password):
        """
        authenticate user password by checking if the user exist

        Args:
            username :username used to login
            login_password:password for the user
        """
        for user in Users.users_list:
           if user.username == username and user.login_password == login_password:
                return True
        return False   