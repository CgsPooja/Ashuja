from selenium.webdriver import  Chrome
from time import sleep

#ws to print parent and child tab title
driver = Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "//a[.='Facebook']").click()
sleep(2)
driver.find_element("xpath", "//a[.='Google+']").click()
sleep(2)
driver.find_element("xpath", "//a[.='Twitter']").click()
sleep(2)
ids = driver.window_handles
for id in ids:
    driver.switch_to.window(id)
    sleep(3)
    print(driver.title)
#Demo Web Shop
#nopCommerce (@nopCommerce) / X
#NopCommerce | Facebook
#What you need to know about the sunset of consumer Google+ on April 2 | Google Workspace Blog
