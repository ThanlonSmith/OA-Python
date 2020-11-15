"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: 添加图片.py
@time: 2020/11/15 下午5:08
"""
from docx import Document

document = Document()
document.add_picture(image_path_or_stream='./imgs/jujingyi.jpeg')
document.save('./result/添加图片.docx')
