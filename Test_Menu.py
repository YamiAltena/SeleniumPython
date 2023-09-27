from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
import log


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')


class Menu(unittest.TestCase):


        
    def setUp(self):
        self.driver = webdriver.Chrome(options = options)
        
    
    def test_Menu_Admin(self):
        log.test_login(self.driver)
        log.Menu_Admin(self.driver)
        time.sleep(3)
        management = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]').text
        self.assertIn('User Management', management)
        print("Successfully go to Menu Admin")

    def test_Menu_PIM(self):
        log.test_login(self.driver)
        log.Menu_PIM(self.driver)
        time.sleep(3)
        Information = self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5').text
        self.assertIn('Employee Information', Information)
        print("Successfully go to Menu PIM")

    def test_Menu_MyInfo(self):
        log.test_login(self.driver)
        log.Menu_Myinfo(self.driver)
        time.sleep(3)
        Personal = self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6').text
        self.assertIn('Personal Details', Personal)
        print("Successfully go to Menu My Info")

    def test_Menu_Claim(self):
        log.test_login(self.driver)
        log.Menu_Claim(self.driver)
        time.sleep(3)
        Claim = self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
        self.assertIn('Claim', Claim)
        print("Successfully go to Menu Claim")


    def tearDown(self):
        self.driver.quit()

    
if __name__ == '__main__':
    unittest.main() 
        