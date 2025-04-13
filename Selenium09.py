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

URL='https://the-internet.herokuapp.com/upload'
driver.get(URL)
driver.maximize_window()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"file-upload")))


dosya_sec=driver.find_element(By.ID,'file-upload')
file_path=r"C:\Users\ondre\Downloads\qq.PNG" # r: rawstring
dosya_sec.send_keys(file_path)
sleep(1)


upload_button=driver.find_element(By.ID,'file-submit')
upload_button.click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div/h3')))

yazi=driver.find_element(By.XPATH,'//*[@id="content"]/div/h3')
dosya_adi=driver.find_element(By.ID,'uploaded-files')

print(yazi.text)
print(dosya_adi.text)

sleep(2)
driver.quit()







