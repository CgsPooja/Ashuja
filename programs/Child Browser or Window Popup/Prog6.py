#ws to close all child tab

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
ids = driver.window_handles         #[parent_id, child1_id, child2_id, child3_id]
for id in ids[1:]:
    driver.switch_to.window(id)
    sleep(2)
    driver.close()