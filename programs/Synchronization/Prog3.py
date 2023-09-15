#example on implicit wait

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("file:///C:/Users/Admin/Downloads/loading.html")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element("name", "fname").send_keys("automation")
driver.find_element("name", "lname").send_keys("automation@123")
"""