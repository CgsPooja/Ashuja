#ws to extract specific row and column cell value

from xlrd import *
from selenium.webdriver import Chrome
from time import sleep

wb = open_workbook("../../excel/sample.xls")
sh = wb.sheet_by_name("Sheet1")
data = sh.row_values(2,0,1)
print(data)
#'sample@1234'
