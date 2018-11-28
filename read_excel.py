import xlrd
book = xlrd.open_workbook('Book1.xls')
sheet = book.sheet_by_index(0)
matrix = [[0]*sheet.ncols for i in range(sheet.nrows)]
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        matrix[i][j] = float(sheet.cell_value(rowx=i, colx=j))
print(matrix)
