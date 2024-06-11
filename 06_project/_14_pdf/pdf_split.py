import fitz
from pathlib import Path
from typing import Union, Tuple
import os


def split_pdf(pdf_file: Union[str, Path, None],
              split_pdf_dir: Union[str, Path],
              split_mode: str,
              split_range_list: Tuple[Tuple[int]]
              ):
    '''
    把一个pdf文件分拆成多个pdf文件，
    :param pdf_file: 被分拆的pdf文件
    :param split_pdf_dir: 分拆后的pdf文件存放的文件夹
    :param split_mode: 分拆模式，single还是other，single的分成一页一页的
    :param split_range_list: 格式是((1,3),(5,7),(9,12))就是某几页拆成一部分
    :return:
    '''
    count = 0
    with fitz.Document(pdf_file) as pdf:
        page_no_width = len(str(pdf.page_count))
        for start, stop in split_range_list:
            if split_mode == 'single':
                _split_pdf_file = os.path.join(split_pdf_dir, f'{pdf_file.stem}-split-P{start + 1:0{page_no_width}d}.pdf')
            else:
                if not stop:
                    stop = pdf.page_count - 1
                _split_pdf_file = f'{split_pdf_dir / pdf_file.stem}-split-' \
                                  f'P{start + 1:0{page_no_width}d}-{stop + 1:0{page_no_width}d}.pdf'

            with fitz.Document() as _split_pdf:
                _split_pdf.insert_pdf(pdf, from_page=start, to_page=stop)
                _split_pdf.save(_split_pdf_file)

if __name__ == '__main__':
    split_pdf(Path("D:/app/pdf/第八单元真题圈_merged.pdf"), 'D:/app/pdf', 'single', ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)))