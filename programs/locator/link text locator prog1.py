#ws to click on facebook linkin dummy webpage

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("file:///C:/Users/Dell/Downloads/Demo%20Web%20Page.html")
link = driver.find_element("link text", "Facebook")
sleep(3)
link.click()
sleep(3)
driver.close()