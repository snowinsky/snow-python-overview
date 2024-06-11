# pip install pymupdf
# pip install pdf2docx

import fitz  # PyMuPDF
from pdf2docx import Converter

def pdf2word(pdf_path, word_path):
    cv = Converter(pdf_path)
    cv.convert(word_path)  # all pages by default
    cv.close()


if __name__ == "__main__":
    # 定义输入的PDF文件路径和输出的Word文件路径
    pdf_path = "D:/ws-py/第八单元打印资料/四下第八单元基础默写.Merged.pdf"
    word_path = "D:/ws-py/111.docx"
    # 执行转换操作
    pdf2word(pdf_path, word_path)
