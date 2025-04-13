from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

URL='https://store.steampowered.com/charts/mostplayed/?l=turkish'
driver.get(URL)
driver.maximize_window()
sleep(4)
#driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")#en yukardan asağı
#sleep(3)
#driver.execute_script("window.scrollTo(document.documentElement.scrollHeight,0);")#asağıdan yukarı
#oyun_40=driver.find_element(By.XPATH,'//*[@id="page_root"]/div[3]/div/div/div/div[3]/table/tbody/tr[40]/td[3]/a/div')
#driver.execute_script("arguments[0].scrollIntoView();" ,oyun_40)
driver.execute_script("window.scrollBy(0,800);")
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
sleep(3)
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.HOME)

sleep(2)
driver.quit()