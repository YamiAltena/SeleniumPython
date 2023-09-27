from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
import log


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')



Menu_Admin_XPATH = '//a[@href="/web/index.php/admin/viewAdminModule"]'
Menu_PIM_XPATH = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
Menu_MYinfo_XPATH = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
Menu_Maintenance_XPATH = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'

class Menu(unittest.TestCase):
        
    def setUp(self):
        self.driver = webdriver.Chrome(options = options)
    
    
    def test_Menu_Admin(self):
        log.test_login(self.driver)
        self.driver.find_element(By.XPATH,Menu_Admin_XPATH).click()
        time.sleep(3)
        management = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]').text
        self.assertIn('User Management', management)

    def test_Menu_PIM(self):
        log.test_login(self.driver)
        self.driver.find_element(By.XPATH,Menu_PIM_XPATH).click()
        time.sleep(3)
        PIM = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
        self.assertIn('PIM', PIM)

    def test_Menu_MyInfo(self):
        log.test_login(self.driver)
        self.driver.find_element(By.XPATH,Menu_MYinfo_XPATH).click()
        time.sleep(3)
        PIM = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
        self.assertIn('PIM', PIM)

    def test_Menu_Maintenance(self):
        log.test_login(self.driver)
        self.driver.find_element(By.XPATH,Menu_Maintenance_XPATH).click()
        time.sleep(3)
        PIM = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
        self.assertIn('PIM', PIM)


    def tearDown(self):
        self.driver.quit()

    
if __name__ == '__main__':
    unittest.main() 
        