import time
from selenium.webdriver import Chrome

#ws to minimize & maximize a window

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.fb.com")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.close()