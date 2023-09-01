"""wp to create a dictionary option index as key and option should be a list of words from customer type DD
https://www.indiapost.gov.in/VAS/Pages/CustomerLinking.aspx
{1:['Bill','an', 'COD', 'customer'], 2:[..], .. }"""

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()