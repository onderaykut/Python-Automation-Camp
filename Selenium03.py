from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

site_URL='https://www.google.com.tr/'
driver.get(site_URL)
sleep(3)
driver.maximize_window()
search_box=driver.find_element(By.ID,'APjFqb')
search_box.send_keys('github')
search_box.send_keys(Keys.ENTER)  #enter=\ue007

sleep(3)

driver.quit()
