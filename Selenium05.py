from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

site_URL='https://tr.wikipedia.org/wiki/Anasayfa'
driver.get(site_URL)

driver.maximize_window()
#driver.find_element(By.XPATH,'//*[@id="mp-itn"]/ul/li[1]/a[2]').click()
search_box=driver.find_element(By.NAME,'search')
search_box.send_keys('atatürk')
sleep(5)
s_button=driver.find_element(By.XPATH,'//*[@id="searchform"]/div/button')
s_button.send_keys(Keys.ENTER)
#s_button.click()
#driver.find_element(By.CLASS_NAME, 'searchButton').click()

sleep(2)

driver.quit()
