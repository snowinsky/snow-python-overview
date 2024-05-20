import requests

res = requests.get("https://www.baidu.com")
res_text = res.text # 返回html格式的文本，而后可以使用正则表达式，lxml或者beautiful Soap来解析html，获得自己想要的结果



from bs4 import BeautifulSoup
soup = BeautifulSoup(res_text, 'html.parser')
inputs = soup.find_all('input')
