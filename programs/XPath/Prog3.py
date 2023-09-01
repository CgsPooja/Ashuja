#ws to automate pharmacy in medplus

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.medplusmart.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//h6[.='Pharmacy']").click()
sleep(3)
driver.find_element("xpath", "//a[.='Upload your Prescription']").click()
sleep(3)
driver.find_element("xpath", "//input[@name='mobileNumber']").send_keys("8456372890")
sleep(3)
driver.find_element("xpath", "//button[.='Send OTP']").click()
sleep(2)
driver.close()
