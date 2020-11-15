"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: 可变长度表方案.py
@time: 2020/11/15 下午4:27
"""
from docx import Document

document = Document()

# 添加表
table = document.add_table(1, 3)

# 填充标题行
heading_cells = table.rows[0].cells
heading_cells[0].text = 'Qty'
heading_cells[1].text = 'SKU'
heading_cells[2].text = 'Description'

# 为每个项添加数据行
items = (
    (7, '1024', 'Plush kittens'),
    (3, '2042', 'Furbees'),
    (1, '1288', 'French Poodle Collars, Deluxe'),
)
for item in items:
    cells = table.add_row().cells
    cells[0].text = str(item[0])
    cells[1].text = item[1]
    cells[2].text = item[2]
"""
for row in table.rows:
    for cell in row.cells:
        print(cell.text)
"""
# 上面看的不太明显,所以保存在表格中查看更方便
document.save('./result/可变长度表方案.docx')
