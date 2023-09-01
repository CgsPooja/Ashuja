#ws to search for watch in demowebshop

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
name = driver.find_element("name", "q")
sleep(2)
name.send_keys("watch")
sleep(5)
driver.close()

