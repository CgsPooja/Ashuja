#ws to click on login and enter all the details.

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.swiggy.com")
driver.maximize_window()
driver.find_element("class name", "x4bK8").click()
sleep(2)
driver.find_element("name","mobile").send_keys("8788040703")
sleep(2)
driver.find_element("class name","a-ayg").click()
sleep(2)
driver.find_element("name","name").send_keys("Automation")
sleep(2)
driver.find_element("id","email").send_keys("auto@mailinator.com")
sleep(2)
driver.find_element("class name","a-ayg").click()
sleep(10)
driver. find_element_by_id("class name","")