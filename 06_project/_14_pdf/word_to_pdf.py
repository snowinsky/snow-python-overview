# pip install docx2pdf

# Python3 program to convert docx to pdf
# using docx2pdf module

# Import the convert method from the
# docx2pdf module
from docx2pdf import convert

def doc2pdf(word_file, pdf_path):

    # Converting docx present in the same folder
    # as the python file
    convert(word_file, pdf_path)

    # # Converting docx specifying both the input
    # # and output paths
    # convert("GeeksForGeeks\GFG_1.docx", "Other_Folder\Mine.pdf")
    #
    # # Notice that the output filename need not be
    # # the same as the docx
    #
    # # Bulk Conversion
    # convert("GeeksForGeeks\")

if __name__ == '__main__':
    '''
    不行，不能用。如果word中都是图片，根本没法转pdf。还是直接用word或者wps打开另存为pdf吧。
    好多的转换方案都是垃圾。。。。
    '''
    # doc2pdf('C:/Users/Jack.Ji/Documents/Doc1.docx', 'C:/Users/Jack.Ji/Documents/Doc1.pdf')