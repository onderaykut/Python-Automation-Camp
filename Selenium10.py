from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

URL='https://dosya.co/'
driver.get(URL)
driver.maximize_window()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"my_file_element")))

driver.save_screenshot("images.png") ## SS ALMA

yukle=driver.find_element(By.ID,'my_file_element')
file_path=r"C:\Users\ondre\Downloads\qq.PNG"
yukle.send_keys(file_path)
sleep(3)

driver.find_element(By.XPATH,'//*[@id="upload_controls"]/tbody/tr[4]/td[2]/input').click()
sleep(5)
link=driver.find_element(By.ID,'ic0-')
print(link.text)
screen_shot=driver.find_element(By.XPATH,'/html/body/div[2]/table')
screen_shot.screenshot("images2.png") # partial ss
#//*[@id="upload_controls"]/tbody/tr[4]/td[2]/input

sleep(3)
driver.quit()
















