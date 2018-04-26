class User(object):
    """Enable the user register and login"""

    def __init__(self):
        self.users = {}                    
    
    def create_account(self, fname, lname, email, pwd):
        self.users[email] = [fname, lname, pwd]
    
    def login(self, email, password):
        if email and password not in self.users:
            return 'email and password incorrect'
        return True   
    