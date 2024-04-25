# pip install PyPDF2
import PyPDF2

pdf_files = [
    "D:/ws-py/snow-python-overview/animals.pdf",
    "D:/ws-py/snow-python-overview/merged.pdf",
]  # PDF 文件列表

out_merge_pdf = str(list(pdf_files)[0]) + "_merged.pdf"

# 创建一个空的 PDF 文档对象
# merged_pdf = PyPDF2.PdfFileMerger(fileobj="mergeFile.pdf")
merged_pdf = PyPDF2.PdfMerger()

# 遍历 PDF 文件列表，读取每个文件的内容并追加到新创建的 PDF 文档对象中
for pdf_file in pdf_files:
    with open(pdf_file, "rb") as file:
        merged_pdf.append(file)

# 将合并后的 PDF 写入到新文件中
with open(out_merge_pdf, "wb") as merged_file:
    merged_pdf.write(merged_file)
