#ws to print tool tip of englisg link in wikipedia

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.wikipedia.org/")
english = driver.find_element("xpath", "(//a[@class='link-box'])[1]")
avalue = english.get_attribute("title")
print(avalue)           #English — Wikipedia — The Free Encyclopedia