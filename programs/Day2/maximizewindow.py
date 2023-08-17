from time import sleep
from selenium.webdriver import Chrome

#ws to maximize a window

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.fb.com")
sleep(3)
driver.maximize_window()
sleep(3)
driver.close()