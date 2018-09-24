import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.accounts import add_account, login

class AccountTest(unittest.TestCase):
    """
    This class tests the login and create account functions
    """
    def test_if_user_created_account_successfully(self):
        name = "Eubule"
        email = "eubule@gmail.com"
        password = "eubulE1."
        self.assertEquals(add_account(name, email, password), "Successfully Added an account")

    def test_returns_error_if_password_is_weak(self):
        name = "Eubule"
        email = "eubule@gmail.com"
        password = "eubulE1"
        self.assertEquals(add_account(name, email, password), "Weak password. Password must contain at least one upper case, lower case and a special caracter")

    def test_returns_error_if__password_is_less_than_6_characters(self):
        name = "Eubule"
        email = "eubule@gmail.com"
        password = "eubul"
        self.assertEquals(add_account(name, email, password), "Invalid password. Password must be at least 6 characters long")
    
    def test_return_error_if_user_attempts_create_account_for_existing_email(self):
        name = "Eubule"
        email = "eubule@gmail.com"
        password = "eubulE1."
        self.assertEquals(add_account(name, email, password), "User with email {} already exist".format(email))
    
    def test_if_user_loged_in_successfully(self):
        email = "eubule@gmail.com"
        password = "eubulE1."
        self.assertEquals(login(email, password), "You have successfully logged in")
    
    def test_if_user_tries_to_log_in_with_wrong_email(self):
        email = "eubu@gmail.com"
        password = "eubulE1."
        self.assertEquals(login(email, password), "You do not have an account with {}".format(email))
    
    def test_if_user_tries_to_log_in_with_wrong_password(self):
        email = "eubule@gmail.com"
        password = "eubulE1>"
        self.assertEquals(login(email, password), "Invalid password. Please enter the correct password")

