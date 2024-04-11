#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# xlrd、xlwt、xlutils 各自的功能都有局限性，但三者互为补充，覆盖了Excel文件尤其是 .xls 文件的操作。xlwt 可以生成 .xls 文件，xlrd 可以读取已经存在的 .xls 文件，xlutils 连接 xlrd 和 xlwt 两个模块，使用户可以同时读写一个 .xls 文件。简单来说，xlrd 负责读、xlwt 负责写、xlutils 负责提供辅助和衔接
# xlwings 能够非常方便的读写 Excel 文件中的数据，并且能够进行单元格格式的修改
# XlsxWriter 是一个用来写 .xlsx 文件格式的模块。它可以用来写文本、数字、公式并支持单元格格式化、图片、图表、文档配置、自动过滤等特性。但不能用来读取和修改 Excel 文件
# openpyxl 通过 工作簿 “workbook - 工作表 sheet - 单元格 cell” 的模式对 .xlsx 文件进行读、写、改，并且可以调整样式
# pandas 大家都不陌生，是进行数据处理和分析的强大模块，有时也可以用来自动化处理Excel

# windows 系统下用xlwings，其他系统下用openpyxl吧，如果想未来和数据分析联动，就用pandas。

# 都是非标准库，需要pip安装
# pip install xlrd
# pip install xlwt
# pip install xlutils
# pip install xlwings
# pip install XlsxWriter
# pip install openpyxl
# pip install pandas



import pandas as x_panda

xlsx_path = "D:/ws-py/snow-python-overview/01_hello_world/files/xls_temp.xlsx"
#########################   xlwings  #########################
import xlwings as x_wing

try:
    app = x_wing.App(visible=True, add_book=False) # 程序可见，只打开不新建工作薄, 好像需要用到office应用程序环境
    app.display_alerts = False # 警告关闭
    app.screen_updating = False # 屏幕更新关闭
    wb = app.books.add()
    wb = app.books.open(xlsx_path)
    wb.sheets['sheet1'].range('A1').value='人生'
    wb.save(xlsx_path)
    wb.save() # 保存文件
    wb.close() # 关闭文件
    app.quit() # 关闭程序
except BaseException as e:
    print(e)
    
    
#########################   xlwings  #########################


#########################   openpyxl  #########################
import openpyxl as x_open

wb = x_open.load_workbook(xlsx_path)
ws1 = wb['Sheet1']
print(ws1['A1'])
ws1['A1'] = 42
ws1['A2'] = '042'

for row in ws1.rows:
    cellValue = [];
    for cell in row:
        cellValue.append(str(cell.value))
    print(',   '.join(cellValue))


ws2 = wb.create_sheet('Sheet2')
for x in range(10):
    ws2['A' + str(x+1)] = x

wb.save(xlsx_path)
#########################   openpyxl  #########################
#########################   pandas  #########################
#########################   pandas  #########################