#ws to click on facebook, twitter, google+ link and switch to twitter page then click on settings
#https://demowebshop.tricentis.com/

from selenium.webdriver import  Chrome
from time import sleep
driver = Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "//a[.='Facebook']").click()

driver.find_element("xpath", "//a[.='Google+']").click()

driver.find_element("xpath", "//a[.='Twitter']").click()

mns = driver.window_handles
for m in mns[2:len(mns)]:
    driver.switch_to.window(m)
    print(driver.title)
driver.find_element("xpath", "//a[@aria-label='Settings']").click()


