import os
import pathlib
from asyncio import Queue
from multiprocessing import Process
from pathlib import Path
from typing import List

import fitz


class PdfMerge(object):
    def __init__(self):
        self.name = 'pdf_merge'

    def merge_pdf(self, pdf_list: List[Path], merged_pdf_file: Path):
        with fitz.Document() as merged_pdf:
            for pdf_no, pdf_file in enumerate(pdf_list, start=1):
                with fitz.Document(str(pdf_file)) as pdf:
                    merged_pdf.insert_pdf(pdf)
            merged_pdf.save(merged_pdf_file)


if __name__ == '__main__':
    PdfMerge().merge_pdf([Path('D:/app/pdf/第八单元真题圈1.pdf'), Path('D:/app/pdf/第八单元真题圈2.pdf')],
                         Path('D:/app/pdf/第八单元真题圈_merged.pdf'))

    # pdfmerge = PdfMerge()
    # q = Queue()
    # pdfmerge.merge_pdf(q, [Path('D:/app/pdf/第八单元真题圈1.pdf'), Path('D:/app/pdf/第八单元真题圈2.pdf')], Path('D:/app/pdf/第八单元真题圈_merged.pdf'))
    # q.join()
