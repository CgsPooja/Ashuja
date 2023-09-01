#ws to search for chicken and click 1st link

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.licious.in/search"
           )
driver.maximize_window()
sleep(2)
driver.find_element("css selector", "input[class='RealSearchBar_searchbar__zap4G']").send_keys("chicken")
sleep(3)
driver.find_element("css selector", "div[class='SearchProductTile_item_description__e3i11']").click()
driver.quit()