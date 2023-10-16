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
        invalid = self.driver.find_element(By.ID,'app').text
        self.assertIn('Invalid credentials', invalid)
    
    def test_logout(self):
        log.URL(self.driver)
        self.driver.implicitly_wait(5)
        log.test_user(self.driver)
        time.sleep(3)
        log.logout(self.driver)
        time.sleep(5)    
        login_button = self.driver.find_element(By.XPATH,'//button[@type="submit"]').text
        self.assertIn('Login', login_button)

    def tearDown(self):
        self.driver.quit()

    
if __name__ == '__main__':
    unittest.main() 