#ws to pritint text of women in ajio

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.ajio.com/")
driver.maximize_window()
foot = driver.find_element("xpath", "//a[@href='/shop/women']")
print(foot.text)                #WOMEN