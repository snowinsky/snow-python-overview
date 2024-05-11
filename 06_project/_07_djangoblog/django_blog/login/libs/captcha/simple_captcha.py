from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, string, os
from io import BytesIO


class Captcha(object):
    def __init__(self):
        self._dir = os.path.dirname(__file__)
        self._captcha_fonts_path = os.path.join(self._dir, "fonts", "Arial.ttf")
    
    @staticmethod
    def instance():
        if not hasattr(Captcha, "_instance"):
            Captcha._instance = Captcha()
        return Captcha._instance

    # 获取随机4个字符组合
    @staticmethod
    def getRandomChar(char_count=4):
        chr_all = string.ascii_letters + string.digits
        chr_4 = "".join(random.sample(chr_all, char_count))
        return chr_4

    # 获取随机颜色
    @staticmethod
    def getRandomColor(low, high):
        return (
            random.randint(low, high),
            random.randint(low, high),
            random.randint(low, high),
        )

    # 制作验证码图片
    def getPicture(self):
        width, height = 180, 60
        # 创建空白画布
        image = Image.new("RGB", (width, height), self.getRandomColor(20, 100))
        # 验证码的字体
        font = ImageFont.truetype(self._captcha_fonts_path, 40)
        # 创建画笔
        draw = ImageDraw.Draw(image)
        # 获取验证码
        char_4 = self.getRandomChar(4)
        # 向画布上填写验证码
        for i in range(4):
            draw.text(
                (40 * i + 10, 0),
                char_4[i],
                font=font,
                fill=self.getRandomColor(100, 200),
            )
        # 绘制干扰点
        for x in range(random.randint(200, 600)):
            x = random.randint(1, width - 1)
            y = random.randint(1, height - 1)
            draw.point((x, y), fill=self.getRandomColor(50, 150))
        # 模糊处理
        image = image.filter(ImageFilter.BLUR)
        # image.save("./%s.jpg" % char_4) #直接保存成图片到当前位置
        out = BytesIO()
        image.save(out, format='JPEG')
        image.close()
        return char_4, out.getvalue() #返回两个结果，一个是string类型的，一个是二进制类型的
        


if __name__ == "__main__":
    Captcha.instance().getPicture()
    
    
