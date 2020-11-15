"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: 逐步向表中添加行.py
@time: 2020/11/15 下午4:04
"""
from docx import Document

document = Document()
table = document.add_table(2, 2)
print('当前的行列数：{}{}'.format(len(table.rows), len(table.columns), ))
table.add_row()  # 默认加10行
print('当前的行列数：{}{}'.format(len(table.rows), len(table.columns), ))
"""
当前的行列数：22
当前的行列数：32
"""
