# pip install python-docx
# from docx import Document
# #from docx.enum.ole import OLE_PACKAGE

# docxfile = Document("D:/doc/DDAP/chinapay/贷后管理上海银联项目-查询贷后资金流向.docx")
# for paragraph in docxfile.paragraphs:
#     print(paragraph.title)
#     for run in paragraph.runs:
#         if run._element.tag.endswith("object"):
#             print('ss')
#             # #if OLE_PACKAGE in run._element.ole_object.type:
#             #     print("Found OLE object of type Excel.")


# import olefile


# def read_excel_from_word_docx(docx_file):
#     ole = olefile.OleFileIO(docx_file)
#     for stream in ole.listdir():
#         if stream[0].lower() == "word/embeddings" and "excel" in stream[1].lower():
#             stream_name = stream[0] + "/" + stream[1]
#             data = ole.openstream(stream_name).read()
#             with open("MCC+mapping+with+loan+usage.xlsx", "wb") as f:
#                 f.write(data)


# import pandas as pd


# def read_excel_data(file_path):
#     data = pd.read_excel(file_path)
#     return data


# # 从example.docx中提取Excel数据
# read_excel_from_word_docx("D:/doc/DDAP/chinapay/贷后管理上海银联项目-查询贷后资金流向.docx")
# data = read_excel_data("MCC+mapping+with+loan+usage.xlsx")
# print(data.head())


from zipfile import ZipFile
import shutil

filename = "D:/doc/DDAP/chinapay/贷后管理上海银联项目-查询贷后资金流向.docx"
with ZipFile(filename, "r") as zip_file:
    for name in zip_file.namelist():
        print(name)
        if not name.startswith("word/embeddings/"):
            continue
        with zip_file.open(name) as f:
            if(f.name.endswith(".xlsx")):
                shutil.copyfile(f, filename + "_01.xlsx")
            