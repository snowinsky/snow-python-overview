import cv2
import numpy as np
import pytesseract
from PIL import Image

## pip install opencv-python

def clearImage(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    # 模糊图像
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    # 锐化图像
    sharpened = cv2.addWeighted(image, 3, blurred, -3, 0)
    # 显示处理后的图像
    # cv2.imshow('Original', image)
    # cv2.imshow('Blurred', blurred)
    cv2.imshow('Sharpened', sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# import cv2
# # 读取图像
# img = cv2.imread('D:/ws-py/第八单元打印资料/第八单元真题圈1-P1.png', cv2.IMREAD_GRAYSCALE)
# # 直方图均衡化
# equ = cv2.equalizeHist(img)
# # 高斯滤波器（模糊）
# blur = cv2.GaussianBlur(img, (5, 5), 0)
# # 中值滤波器（去噪）
# median = cv2.medianBlur(img, 5)
# # 显示结果
# cv2.imshow('Original', img)
# cv2.imshow('Histogram Equalization', equ)
# cv2.imshow('Gaussian Blur', blur)
# cv2.imshow('Median Blur', median)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

### pip install pytesseract pillow tesseract
def extract_text_from_image(image_path):

    # 读取图像
    image = cv2.imread(image_path)
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 进行二值化处理
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # 使用Tesseract OCR引擎进行文字识别
    text = pytesseract.image_to_string(Image.fromarray(thresh))
    print(text)

if __name__ == '__main__':
    image_path = 'D:/ws-py/diba1-P1.png'

    text = pytesseract.image_to_string(image=Image.open(image_path), lang='eng+chi_sim')
    print(text)