# pip install img2pdf
import img2pdf
import time

images = [
    "D:/doc/PLUM/人教版数学四年级第四单元测试/1.png",
    "D:/doc/PLUM/人教版数学四年级第四单元测试/2.png",
    "D:/doc/PLUM/人教版数学四年级第四单元测试/3.png",
    "D:/doc/PLUM/人教版数学四年级第四单元测试/4.png"
]

def build_outpath_by_inpath(inpaths: list):
    if(inpaths == None or len(inpaths) == 0):
        return time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".pdf"
    else:
        return str(inpaths[0]) + ".pdf"
    
    
    
output = build_outpath_by_inpath(images)

print(output)
 

# 创建一个PDF文件 并以二进制方式写入
with open(output, "wb") as f:
    # convert函数 用来转PDF
    write_content = img2pdf.convert(images)
    f.write(write_content)  # 写入文件
print("转换成功！")  # 提示语
