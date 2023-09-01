#ws to get the attribute of href

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://www.wikipedia.org/")
english = driver.find_element("xpath", "(//a[@class='link-box'])[1]")
avalue = english.get_attribute("href")
print(avalue)           #https://en.wikipedia.org/