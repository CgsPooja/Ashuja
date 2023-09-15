#ws to download a python in python.org

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("prefs", {"safebrowsing.enabled": True})
driver = Chrome(options=opts)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "(//a[.='Download Python 3.11.5'])[3]").click()
sleep(2)
driver.close()



