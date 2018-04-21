class User(object):

    def __init__(self):
        self.users = {}
    
    def create_account(self, fname, lname, email, pwd):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.pwd = pwd
        self.users[self.email] = [self.fname, self.lname, self.pwd]
    