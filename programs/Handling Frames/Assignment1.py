#navigate to below application and click on adhar tweet on right navigation panel
#https://uidai.gov.in/en/

from selenium.webdriver import Chrome
from time import sleep
driver = Chrome()
driver.get("https://uidai.gov.in/en/")
driver.maximize_window()
sleep(4)
driver.find_element("xpath", "//span[@class='close']").click()
tweet = driver.find_element("xpath", "//iframe[@id='twitter-widget-0']")
driver.switch_to.frame(tweet)
sleep(5)
driver.find_element("xpath", "//span[.='Tweets from @UIDAI']").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
sleep(12)
follow = driver.find_element("xpath", "(//a[@role='link'])[9]/div/span/span/span")
print(follow.text)
#4,371
