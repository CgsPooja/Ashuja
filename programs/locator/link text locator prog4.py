#ws to click on travel info and metro timings in bmrcl

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://english.bmrc.co.in/#/")
driver.maximize_window()
sleep(2)
driver.find_element("link text", "FINANCE").click()
sleep(2)
driver.find_element("link text", "Bonds").click()
sleep(5)
driver.quit()