#wp to create a dictionary "username" as key and "password" as value
#withput comprahension

from xlrd import *
from selenium.webdriver import Chrome
from time import sleep

d = {}
wb = open_workbook("../../excel/sample.xls")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows
for i in range(1, row_count):
    data = sh.row_values(i)
    d[data[0]] = data[1]
print(d)
#{'demo': 'demo@123', 'sample': 'sample@1234', 'automation': 'automation123', 'admin': 'manager', 3543.0: '%$GFY^%$'}

#with comprahension

wb = open_workbook("../excel/sample.xlsx")
sh = wb.sheet_by_name("Sheet1")
d = { sh.row_values(i)[0]:sh.row_values(i)[1] for i in range(1, sh.nrows) }     ##['sample', 'sample@1234'][0] : #['sample', 'sample@1234'][1] -> sample:sample@1234
print(d)
#{'demo': 'demo@123', 'sample': 'sample@1234', 'automation': 'automation123', 'admin': 'manager', 3543.0: '%$GFY^%$'}