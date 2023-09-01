#ws to select all the options from a DD

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
ssdd = driver.find_element("id", "a1")
s = Select(ssdd)
ops = s.options
print(ops)      #[<selenium.webdriver.remote.webelement.WebElement (session="96bfe0ae41594d21c2f3cf417dd56eb9", element="EB5243B0D3BE44F5531120EB7509ECE1_element_4")>, ... ]