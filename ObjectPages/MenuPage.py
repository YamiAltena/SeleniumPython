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



        
    









     











      


