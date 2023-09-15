from selenium.webdriver import  Chrome
from time import sleep

#ws to print parent and child tab address
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
pid = driver.current_window_handle     #47131BE41C0A298ABB40F5DC259FAA88
print(pid)
ids = driver.window_handles      #['47131BE41C0A298ABB40F5DC259FAA88', '162FDBF60A9E6D694ADFE98D634F1795', '2116BF367785D8E726B71CCAC0E58F4F', '1BBB013FDC47F93DF9457ADA29DE9CED']
print(ids)