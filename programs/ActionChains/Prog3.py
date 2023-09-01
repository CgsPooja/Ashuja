#ws to perform double click on element in sample webpage

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
double = driver.find_element("xpath", "//button[.='Double-Click Me To See Alert']")
a= ActionChains(driver)
sleep(2)
a.double_click(double).perform()