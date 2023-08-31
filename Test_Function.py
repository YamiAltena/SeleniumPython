from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import unittest
import pyautogui


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')
# tanpa membuka browser                     
#options.headless = True


class example(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome(options = options)
    
    def test_move_to_element(self):
        self.driver.maximize_window()
        self.driver.get('https://www.canva.com/')
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH,'//*[@id=":R4kjr:"]/span/div')).perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id=":R4kjrH1:"]/div/div/div/div/div[1]/ul/li[2]/ul/li[3]/a/div').click()
        time.sleep(10)
        assert 'Social Media Marketing & Design Tools for Agencies | Canva' in self.driver.title

    def test_explicty_wait(self):
        self.driver.get('https://demoqa.com/alerts')
        self.driver.find_element('id','timerAlertButton').click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        print('berhasil terpencet')
        time.sleep(3)

    def test_PopUpHandle(self):
        for i in range (2):
            self.driver.get('https://tees.co.id/')
            try:  
                WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,'/html/body/div[1]/div')))
                print('pop up muncul')
                self.driver.find_element('class name','btn-modal-close').click()
                print('pop up berhasil di close')
            except TimeoutException:
                print('pop up tidak ada')
                pass
    
    def test_UploadFile(self):
        self.driver.get('https://demoqa.com/upload-download')
        self.driver.find_element('id','uploadFile').send_keys('C:/Users/Raka/Pictures/friends.jpg')
        time.sleep(3)
        self.driver.switch_to.new_window('tab')
        self.driver.get('https://gofile.io/uploadFiles')
        time.sleep(3)
        self.driver.find_element('id','filesUpload').click()
        time.sleep(3)
        pyautogui.write(r'C:\Users\Raka\Pictures\friends.jpg')
        pyautogui.press('enter')
        time.sleep(3)

    def test_DemoQAandJQuery(self):
        #DemoQA
        self.driver.get('https://demoqa.com/droppable')
        target = self.driver.find_element('id','droppable')
        drag = self.driver.find_element('id','draggable')
        ActionChains(self.driver).drag_and_drop(drag, target).perform()
        self.driver.get('https://demoqa.com/date-picker')
        self.driver.find_element('id','datePickerMonthYearInput').click()
        pyautogui.press('BACKSPACE', presses = 10)
        pyautogui.typewrite('03/19/2023')
        pyautogui.press('ENTER')
        time.sleep(3)
        #JQuery
        self.driver.get('https://jqueryui.com/datepicker/')
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="content"]/iframe'))
        self.driver.find_element('id','datepicker').send_keys('19', Keys.ENTER)
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main() 

    




