#ws to upload resume in naukri.com

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()
sleep(3)
file = driver.find_element("xpath","//input[@type='file']")
file.send_keys(r"E:\books\online_marketing_tutorial.pdf")
sleep(2)
driver.close()