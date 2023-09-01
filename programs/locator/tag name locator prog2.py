#ws to click demowebshop

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.swiggy.com")
driver.maximize_window()
driver.find_element("tag name","a").click()
sleep(5)
driver.close()