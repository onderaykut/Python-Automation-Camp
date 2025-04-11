from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

site_URL='https://store.steampowered.com/charts/mostplayed/?l=turkish'
driver.get(site_URL)

driver.maximize_window()
sleep(5)
oyun=driver.find_elements(By.CLASS_NAME,"_1n_4-zvf0n4aqGEksbgW9N")
for i,x in enumerate(oyun,start=1):
    print('{}. Oyun: {}'.format(i,x.text))

#print(f'Oyun adı: {oyun.text}')
#print(oyun[5].text)




sleep(1)
driver.quit()
