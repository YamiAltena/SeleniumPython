from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def URL(driver):
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.implicitly_wait(5)
    
def test_user(driver):
    driver.find_element(By.NAME,'username').send_keys('Admin')
    driver.find_element(By.NAME,'password').send_keys('admin123' + Keys.RETURN)

def test_login(driver):
    URL(driver)
    test_user(driver)

def test_user_WrongPass(driver):
    driver.find_element(By.NAME,'username').send_keys('Admin')
    driver.find_element(By.NAME,'password').send_keys('admin356' + Keys.RETURN)
        
def logout(driver):
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown").click()
    driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a").click() 

def Teks_Invalid(driver):
    return driver.find_element(By.ID,'app').text
    
def Button(driver):  
    return driver.find_element(By.XPATH,'//button[@type="submit"]').text













