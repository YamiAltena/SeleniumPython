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

def Menu_Admin(driver):
    driver.find_element(By.XPATH,'//a[@href="/web/index.php/admin/viewAdminModule"]').click()

def Menu_PIM(driver):
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()

def Menu_Myinfo(driver):
    driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').click()

def Menu_Claim(driver):
    driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a').click()




