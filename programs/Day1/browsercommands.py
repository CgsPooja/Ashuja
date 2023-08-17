from selenium.webdriver import Chrome
import time
driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.facebook.com")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(5)
driver.close()