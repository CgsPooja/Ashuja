#ws to click on lakme product in lakme

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.lakmeindia.com/")
driver.maximize_window()
sleep(2)
driver.find_element("partial link text", "Look").click()
sleep(5)
driver.quit()