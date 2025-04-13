from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

site_URL='https://store.steampowered.com/charts/mostplayed/?l=turkish'

driver.get(site_URL)
driver.maximize_window()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"_1n_4-zvf0n4aqGEksbgW9N")))

oyun=driver.find_elements(By.CLASS_NAME,"_1n_4-zvf0n4aqGEksbgW9N")
for i,x in enumerate(oyun,start=1):
    print('{}. Oyun: {}'.format(i,x.text))

sleep(1)
driver.quit()