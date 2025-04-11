from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

video_URL='https://www.python.org/'

driver.get(video_URL)

driver.maximize_window() #tam ekran
#driver.get("https://chatgpt.com/")
sleep(2)
driver.execute_script("window.open('https://www.google.com.tr/?hl=tr','_blank');")    #execute_script içinde js kodları calısır
sleep(2)
driver.switch_to.window(driver.window_handles[-1])  #son sekmeye gec
sleep(2)
driver.close() #sekmeyi kapat
#driver.minimize_window()
#driver.back()  #onceki sayfa
#driver.refresh()
#driver.forward()


#print(f"Bulunduğunuz sayfanın linki: {driver.current_url}")
#print(f"Bulunduğunuz sayfanın başlığı: {driver.title}")

sleep(3)
driver.quit()











