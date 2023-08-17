from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../../drivers/chromedriver.exe")
driver.get("https://demowebshop.tricentis.com/")
srch = driver.find_element("name", "")
srch.send_keys("watch")
