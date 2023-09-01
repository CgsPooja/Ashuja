#ws to enter your location in swiggy.com

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.swiggy.com")
sleep(2)
driver.find_element("name", "location").send_keys("kalepadal hadapsar")
sleep(4)
driver.close()
