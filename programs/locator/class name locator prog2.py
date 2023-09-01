#ws to search for goa in flipkart booking

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.flipkart.com/travel/flights?otracker=nmenu_Flights")
driver.maximize_window()
sleep(2)
driver.find_element("class name", "_1w3ZZo._1YBGQV._2EjOJB.lZd1T6._2vegSu._2mFmU7").send_keys("goa")
sleep(5)
driver.close()