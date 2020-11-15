"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: 保持图片宽高比.py
@time: 2020/11/15 下午6:03
"""
from docx.shared import Inches
from docx import Document

document = Document()
document.add_picture(image_path_or_stream='./imgs/jujingyi.jpeg', width=Inches(3.5))
document.save('./result/保持图片宽高比.docx')
