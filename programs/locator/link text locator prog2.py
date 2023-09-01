#ws to click on Today's Deals in amazon

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(2)
link = driver.find_element("link text", "Today's Deals")
sleep(2)
link.click()
sleep(5)
driver.close()
