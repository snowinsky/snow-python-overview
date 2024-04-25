# pip install img2pdf
import img2pdf
import time
import os

images = [
    "D:/doc/PLUM/人教版数学四年级第四单元测试/1.png",
    "D:/doc/PLUM/人教版数学四年级第四单元测试/2.png",
    "D:/doc/PLUM/人教版数学四年级第四单元测试/3.png",
    "D:/doc/PLUM/人教版数学四年级第四单元测试/4.png",
]


##########################################################
def imageList2pdf(images):
    """_summary_

    Args:
        images (_type_): _description_
    """

    def build_outpath_by_inpath(inpaths: list):
        if inpaths == None or len(inpaths) == 0:
            return time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".pdf"
        else:
            return str(inpaths[0]) + ".pdf"

    output = build_outpath_by_inpath(images)

    print("the images will be converted to pdf file=", output)

    # 创建一个PDF文件 并以二进制方式写入
    with open(output, "wb") as f:
        # convert函数 用来转PDF
        write_content = img2pdf.convert(images)
        f.write(write_content)  # 写入文件

    print("转换成功！", output)  # 提示语


##########################################################
def imageFolder2pdf(imageFolder: str):
    """_summary_

    Args:
        imageFolder (str): _description_
    """
    if os.path.isfile(imageFolder):
        imageList2pdf(list(imageFolder))
        return
    imageList = [
        os.path.join(imageFolder, fName) for fName in os.path.listdir(imageFolder)
    ]
    imageList2pdf(imageList)


##########################################################
if __name__ == "__main__":
    p = os.path.join("D:\\doc_backup\\第二单元打印资料\\第二单元打印资料\\src")
    print(os.listdir(p))
