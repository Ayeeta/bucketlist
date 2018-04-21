from src.user import User
import unittest

class TDDInUser(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.user.users = {}

    def test_create_account_method(self):
        self.user.create_account('fname','lname','email','pwd')       
        self.assertIn('email', self.user.users, msg='email not in dict')

