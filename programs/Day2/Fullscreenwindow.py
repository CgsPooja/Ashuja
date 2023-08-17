
import time
from selenium.webdriver import Chrome

#ws to Full Screen a window

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.fb.com")
time.sleep(3)
driver.fullscreen_window()
time.sleep(3)
driver.close()