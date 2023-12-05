from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from ObjectPages import log

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')


class Login(unittest.TestCase):
  
    def setUp(self):
        self.driver = webdriver.Chrome(options = options)

    def test_login(self):
        log.URL(self.driver)
        self.driver.implicitly_wait(5)
        log.test_user(self.driver)
        time.sleep(3)
        assert 'OrangeHRM' in self.driver.title
        
    def test_login_FAILED_WrongPassword(self):
        log.URL(self.driver)
        self.driver.implicitly_wait(5)
        log.test_user_WrongPass(self.driver)
        time.sleep(3)
        invalid = log.Teks_Invalid(self.driver)
        self.assertIn('Invalid credentials', invalid)
    
    def test_logout(self):
        log.URL(self.driver)
        self.driver.implicitly_wait(5)
        log.test_user(self.driver)
        time.sleep(3)
        log.logout(self.driver)
        time.sleep(5)    
        login_button = log.Button(self.driver)
        self.assertIn('Login', login_button)

    def tearDown(self):
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main() 