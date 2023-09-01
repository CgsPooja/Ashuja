"""wp to create a dictionary alphabet and state name pair from passport seva
https://portal2.passportindia.gov.in/AppOnlineProject/user/RegistrationBaseAction?request_locale=en
'A':{'Ahmedaba','Amrithsar'}, 'B':{'Bangalore'},....."""

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome()