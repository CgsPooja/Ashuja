#wp to extract all rows columns/cell values.

from xlrd import *
from selenium.webdriver import Chrome
from time import sleep

wb = open_workbook("../../excel/sample.xls")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows
for i in range(0, row_count):
    data = sh.row_values(i)
    print(data)