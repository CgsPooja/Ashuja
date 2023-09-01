#ws to click on search field and search for facewash

from selenium.webdriver import Chrome
from time import sleep

driver=Chrome()
driver.get("https://mamaearth.in/")
driver.maximize_window()
sleep(5)
src = driver.find_element("xpath", "//p[contains(@class,'styles_typicalWrapper')]")
src.click()
src_txt = driver.find_element("xpath", "//input[@id='searchInputWrapper']")
src_txt.send_keys("facewash")
sleep(5)
driver.close()