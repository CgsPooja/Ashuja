#launch passport seva application

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.nykaa.com/")
driver.maximize_window()
driver.find_element("xpath","//a[@href='https://www.nykaa.com/sp/hair-clp-desktop/hair']").click()
sleep(2)
