"""handle simple alert in alert in below application
https://unifiedportal-epfo.epfindia.gov.in/publicPortal/no-auth/misReport/home/loadSearchTrrnHome"""

from selenium.webdriver import  Chrome
from time import sleep
driver = Chrome()
driver.get("https://unifiedportal-epfo.epfindia.gov.in/publicPortal/no-auth/misReport/home/loadSearchTrrnHome")
driver.maximize_window()
driver.find_element("xpath", "//button[@id='btnFilter']").click()
sleep(2)
alt = driver.switch_to.alert
alt.accept()
sleep(3)
driver.close()
