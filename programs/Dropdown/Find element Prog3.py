#ws to print text all major tabs in amazon

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()
driver = Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
tabs = driver.find_elements("xpath", "//a[@class='nav-a  ']")
for tab in tabs:
    print(tab.text)

"""
Amazon miniTV
Sell
Best Sellers
Today's Deals
Mobiles
New Releases
Customer Service
Prime
Electronics
"""