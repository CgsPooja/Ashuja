#ws to print tool tip of google apps

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.google.com")
account = driver.find_element("xpath", "//a[@class='gb_d']")
value = account.get_attribute("aria-labeler")
print(value)                #Google apps