from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.maximize_window()
src = driver.find_element("id","twotabsearchtextbox")
src.send_keys("watch")
src_btn = driver.find_element("id","nav-search-submit-button")
src_btn.click()