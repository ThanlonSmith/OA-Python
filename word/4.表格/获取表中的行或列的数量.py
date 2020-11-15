"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: 获取表中的行或列的数量.py
@time: 2020/11/15 下午4:00
"""
from docx import Document

document = Document()
table = document.add_table(2, 2)
row_count = len(table.rows)
col_count = len(table.columns)
print(row_count, col_count)
"""
2 2
"""
