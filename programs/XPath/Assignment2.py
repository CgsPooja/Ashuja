#launch spotify application

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://open.spotify.com/")
driver.maximize_window()
driver.find_element("xpath","//button[@class='Button-sc-1dqy6lx-0 eqSwxl sibxBMlr_oxWTfBrEz2G']").click()
sleep(2)

driver.find_element("xpath","//input[@name= 'email']").send_keys("arnav123@mailinator.com")
sleep(2)

driver.find_element("xpath","//input[@id='password']").send_keys("Qaz_12345")
sleep(2)

driver.find_element("xpath","//input[@name='displayname']").send_keys("aaru")
sleep(2)

driver.find_element("xpath","//input[@id='year']").send_keys("1990")
sleep(2)

driver.find_element("xpath","//select[@id='month']").click()
sleep(2)

driver.find_element("xpath","//option[@value='01']").click()
sleep(2)

driver.find_element("xpath","//input[@id='day']").send_keys("10")
sleep(2)

driver.find_element("xpath","//span[@class='Type__TypeElement-sc-goli3j-0 eIvwKg TextForLabel-sc-1wen0a8-0 eygmXy']").click()
sleep(2)

driver.find_element("xpath","//span[@class='Indicator-sc-1airx73-0 jrJQVH']").click()
sleep(2)

driver.find_element("xpath","//span[@class='Indicator-sc-1airx73-0 jrJQVH']").click()
sleep(2)

driver.find_element("xpath","//span[@class='ButtonInner-sc-14ud5tc-0 dqLIWu encore-bright-accent-set SignupButton___StyledButtonPrimary-cjcq5h-1 jazsmO']").click()
sleep(10)
driver.close()