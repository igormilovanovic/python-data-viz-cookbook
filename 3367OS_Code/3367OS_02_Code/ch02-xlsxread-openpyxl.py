from openpyxl import load_workbook

file = 'ch02-xlsxdata.xlsx'

wb = load_workbook(filename=file)

ws = wb.get_sheet_by_name('Sheet1')

dataset = []

for r in ws.rows:
    col = []
    for c in r:
        col.append(c.value)
    dataset.append(col)

from pprint import pprint

pprint(dataset)


