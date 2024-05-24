#pip install captcha

from captcha.image import ImageCaptcha

image = ImageCaptcha(width=280,height=90)
data = image.generate('1234587')
print(data)
image.write('1234587', 'out.png')

