from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()

video_URL='https://tr.wikipedia.org/wiki/Anasayfa'

driver.get(video_URL)
print(driver.title)
sleep(3)
driver.quit()













