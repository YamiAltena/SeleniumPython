from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')


self.driver = webdriver.Chrome(options = options)
 
    def test_login(self):
        self.driver.find_element(By.NAME,'username').send_keys('Admin')
        self.driver.find_element(By.NAME,'password').send_keys('admin123' + Keys.RETURN)


    

