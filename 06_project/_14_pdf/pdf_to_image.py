from pathlib import Path
from typing import Union,Iterable,List
from PIL import Image
from io import BytesIO

import fitz

def pdf2images(pdf_file: Union[str, Path, None], image_dir: Union[str, Path],
        image_format: str, image_alpha: bool, image_quality: int, image_dpi: int, page_range: Iterable
        ):
    zoom = image_dpi / 96 * 4 / 3  # actually 72
    matrix = fitz.Matrix(zoom, zoom)
    with fitz.Document(pdf_file) as pdf:
        page_no_width = len(str(pdf.page_count))
        for page_no in page_range:
            image_file = f'{image_dir / pdf_file.stem}-P{page_no + 1:0{page_no_width}d}.{image_format}'
            image_alpha = False if image_format == 'jpg' else image_alpha
            pixmap = pdf[page_no].get_pixmap(matrix=matrix, alpha=image_alpha)
            if image_format == 'png':
                pixmap.save(image_file)
            else:  # JPEG
                image = Image.open(BytesIO(pixmap.tobytes()))
                image.save(image_file, quality=image_quality, dpi=(image_dpi, image_dpi))
                image.close()


def images2pdf(image_list: List[Union[str, Path]], pdf_file: Union[str, Path]):
    with fitz.Document() as pdf:
        for image_no, image_file in enumerate(image_list, start=1):
            with fitz.Document(image_file) as image_doc:
                pdf_bytes = image_doc.convert_to_pdf()
                with fitz.Document('images.pdf', stream=pdf_bytes) as image_pdf:
                    pdf.insert_pdf(image_pdf)
        pdf.save(pdf_file)

if __name__ == '__main__':
    pdf_file_path = ''
    image_dir = ''
    image_format = 'png'
    image_alpha = False