#ws to click on other lang exist in seleniumdev

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.selenium.dev/downloads/")
driver.maximize_window()
sleep(2)
driver.find_element("partial link text", "languages").click()
sleep(5)
driver.close()