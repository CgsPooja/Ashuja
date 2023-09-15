#example on implicit wait

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://vtu.ac.in/en/?s=vtu+results")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element("xpath", "//span[.='Online Degree']").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
driver.find_element("xpath", "//a[.=' apply now ']").click()
