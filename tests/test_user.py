from src.user import User
import unittest

class TDDInUser(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.usersdict = {} 
        self.session = {}              


    def test_create_account_method(self):
        self.user.create_account('fname','lname','email','pwd')       
        self.assertIn('email', self.user.users, msg='email not in dict')

    def test_login_method(self):
        self.assertTrue(self.user.login('abc@sth.com','pwd123'), msg=None)       
