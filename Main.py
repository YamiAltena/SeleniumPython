from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import log


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options = options)
        self.url = 'https://opensource-demo.orangehrmlive.com/'

    def test_login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        log.test_user(self.driver)
        time.sleep(3)
        assert 'OrangeHRM' in self.driver.title
        
    def test_login_FAILED_WrongPassword(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME,'username').send_keys('Admin')
        self.driver.find_element(By.NAME,'password').send_keys('admin356' + Keys.RETURN)
        time.sleep(3)
        invalid = self.driver.find_element(By.ID,'app').text
        self.assertIn('Invalid credentials', invalid)
    
    def test_logout(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME,'username').send_keys('Admin')
        self.driver.find_element(By.NAME,'password').send_keys('admin123' + Keys.RETURN)
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME,"oxd-userdropdown").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()
        time.sleep(5)    
        login_button = self.driver.find_element(By.XPATH,'//button[@type="submit"]').text
        self.assertIn('Login', login_button)

    def tearDown(self):
        self.driver.quit()



class Menu(unittest.TestCase):
        
    def setUp(self):
        self.driver = webdriver.Chrome(options = options)
    
    def test_Menu_Admin(self):
        log.test_login(self.driver)
        self.driver.find_element(By.XPATH,'//a[@href="/web/index.php/admin/viewAdminModule"]').click()
        time.sleep(3)
        management = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]').text
        self.assertIn('User Management', management)

    def test_Menu_PIM(self):
        log.test_login(self.driver)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(3)
        PIM = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
        self.assertIn('PIM', PIM)

    def test_Menu_MyInfo(self):
        log.test_login(self.driver)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(3)
        PIM = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
        self.assertIn('PIM', PIM)

    def test_Menu_Maintenance(self):
        log.test_login(self.driver)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(3)
        PIM = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
        self.assertIn('PIM', PIM)

    def tearDown(self):
        self.driver.quit()

    
if __name__ == '__main__':
    unittest.main() 