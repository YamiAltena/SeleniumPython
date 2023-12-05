from selenium.webdriver.common.by import By


class MenuPage:
    def Menu_Admin(driver):
        driver.find_element(By.XPATH,'//a[@href="/web/index.php/admin/viewAdminModule"]').click()

    def Menu_PIM(driver):
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()

    def Menu_Myinfo(driver):
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').click()

    def Menu_Claim(driver):
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a').click()


class Assert:

    def Teks_Admin(driver):
        return driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]').text
    
    def Teks_Information(driver):
        return driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5').text
    
    def Teks_Personal(driver):
        return driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6').text
    
    def Teks_Claim(driver):
        return driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6').text




        
    









     











      


