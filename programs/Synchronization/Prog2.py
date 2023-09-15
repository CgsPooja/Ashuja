#example on sleep()

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("file:///C:/Users/Admin/Downloads/loading.html")
driver.maximize_window()
sleep(15)
driver.find_element("name", "fname").send_keys("automation")
driver.find_element("name", "lname").send_keys("automation@123")

"""
*in the above example DOM is visible within 10seconds but it will wait for complete time duration, it is a brawback of lseep.
*to overcome this will go implicitly_wait()
"""