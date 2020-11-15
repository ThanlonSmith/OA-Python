"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: 添加表格.py
@time: 2020/11/15 下午2:47
"""
from docx import Document

document = Document()
table = document.add_table(rows=2, cols=2)
document.save('./result/添加表格.docx')
