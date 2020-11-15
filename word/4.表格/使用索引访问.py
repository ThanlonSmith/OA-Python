"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: 使用索引访问.py
@time: 2020/11/15 下午3:09
"""
from docx import Document

document = Document()
table = document.add_table(rows=2, cols=2)
print(table.rows, type(table.rows))  # <docx.table._Rows object at 0x7f01c117a0d0> <class 'docx.table._Rows'>
row = table.rows[1]
print(row)  # <docx.table._Row object at 0x7f79a666f370>
print(row.cells)  # (<docx.table._Cell object at 0x7fb7b8d41610>, <docx.table._Cell object at 0x7fb7b8d41670>)
row.cells[0].text = 'Foo bar to you.'
row.cells[1].text = 'And a hearty foo bar to you too sir!'
document.save('./result/使用索引访问.docx')
