#example on without synchronization

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("file:///C:/Users/Admin/Downloads/loading.html")
driver.maximize_window()
driver.find_element("name", "fname").send_keys("automation")
driver.find_element("name", "lname").send_keys("automation@123")
#ElementNotInteractableException: Message: element not interactable

"""
*according to above example we will get exception, because application is taking more time to load, but selenium
is fastly trying to perform the action, so we will get execption.
*to handle this we go synchronization.
"""