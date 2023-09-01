#example on xpath in myntra.com

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.myntra.com/kids?f=Categories%3AShirts%3A%3AGender%3Aboys%2Cboys%20girls&plaEnabled=false")
driver.maximize_window()
sleep(3)
driver.find_element("xpath","(//h4[@class='atsa-title'])[3]").click()
sleep(2)

