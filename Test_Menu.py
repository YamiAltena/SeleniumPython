from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
from ObjectPages import log
from ObjectPages.MenuPage import MenuPage
from ObjectPages.MenuPage import Assert


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')


class Menu(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(options = options)
        
    def test_Menu_Admin(self):
        log.test_login(self.driver)
        MenuPage.Menu_Admin(self.driver)
        time.sleep(3)
        Management = Assert.Teks_Admin(self.driver)
        self.assertIn('User Management', Management)
        print("Successfully go to Menu Admin")

    def test_Menu_PIM(self):
        log.test_login(self.driver)
        MenuPage.Menu_PIM(self.driver)
        time.sleep(3)
        Information = Assert.Teks_Information(self.driver)
        self.assertIn('Employee Information', Information)
        print("Successfully go to Menu PIM")

    def test_Menu_MyInfo(self):
        log.test_login(self.driver)
        MenuPage.Menu_Myinfo(self.driver)
        time.sleep(3)
        Personal = Assert.Teks_Personal(self.driver)
        self.assertIn('Personal Details', Personal)
        print("Successfully go to Menu My Info")

    def test_Menu_Claim(self):
        log.test_login(self.driver)
        MenuPage.Menu_Claim(self.driver)
        time.sleep(3)
        Claim = Assert.Teks_Claim(self.driver)
        self.assertIn('Claim', Claim)
        print("Successfully go to Menu Claim")

    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main() 
        