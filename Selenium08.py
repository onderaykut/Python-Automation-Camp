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

URL='https://the-internet.herokuapp.com/javascript_alerts'
driver.get(URL)
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()
#//*[@id="content"]/div/ul/li[1]/button
#//*[@id="content"]/div/ul/li[2]/button
#//*[@id="content"]/div/ul/li[3]/button
WebDriverWait(driver,10).until(EC.alert_is_present())

site_alert=Alert(driver)
sleep(2)
site_alert.send_keys("onder")
sleep(2)
#site_alert.accept()
site_alert.accept()

yazi=driver.find_element(By.ID,'result')
print(yazi.text)


sleep(2)
driver.quit()
