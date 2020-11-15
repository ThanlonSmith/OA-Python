"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: for 循环中直接使用它们.py
@time: 2020/11/15 下午3:34
"""
from docx import Document

document = Document()
table = document.add_table(2, 2)

for row in table.rows:
    for cell in row.cells:
        row.cells[0].text = 'Foo bar to you.'
        row.cells[1].text = 'And a hearty foo bar to you too sir!'
        print(cell.text)
# Console show：
"""
Foo bar to you.
And a hearty foo bar to you too sir!
Foo bar to you.
And a hearty foo bar to you too sir!
"""
