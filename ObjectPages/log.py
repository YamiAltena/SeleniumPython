from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

    
def test_user(driver):
    driver.find_element(By.NAME,'username').send_keys('Admin')
    driver.find_element(By.NAME,'password').send_keys('admin123' + Keys.RETURN)

def test_login(driver):
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.implicitly_wait(5)
    test_user(driver)
    time.sleep(3)






