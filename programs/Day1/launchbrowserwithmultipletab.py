from selenium.webdriver import Chrome
import time
driver = Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://www.bing.com")
time.sleep(3)
# Lets open the second tab
driver.execute_script("window.open('about:blank','secondtab')")
driver.switch_to.window("secondtab")
driver.get('https://www.google.com/')
time.sleep(3)
# Lets open the third tab
driver.execute_script("window.open('about:blank','thirdtab')")
driver.switch_to.window("thirdtab")
driver.get('https://www.facebook.com/')
time.sleep(3)
driver.close()
time.sleep(3)
driver.quit()