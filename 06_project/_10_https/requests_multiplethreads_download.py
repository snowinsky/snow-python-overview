import requests
import os
import time
import threading
from bs4 import BeautifulSoup

class Img_Downloader(object):
    def create_dir(self, dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)


    def url_call(self, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        r = requests.get(url, headers=headers)
        r.encoding = 'gb2312'
        return r.text

    def download_img(self, url):
        html = self.url_call(url)
        soup = BeautifulSoup(html, 'html.parser')
        img_list = soup.find_all('img')
        self.create_dir('img')
        for img in img_list:
            img_alt = img.get('alt')
            img_src = img.get('realsrc')
            if img_alt is None:
                print()
            else:
                print("try to download url=", img_src, img_alt)
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
                r = requests.get(img_src, headers=headers)  # 下载图片，之后保存到文件
                with open('img/{}{}'.format(time.time(), img_src.split('/')[-1]), 'wb') as f:
                    f.write(r.content)
                    time.sleep(1)  # 休息一下，不要给网站太大压力，避免被封

from concurrent.futures import ThreadPoolExecutor

if __name__ == '__main__':
    idx_array = [i for i in range(1, 8)]
    url_base = "https://m.tuiimg.com/meizitu/list_{}.html"
    downloader = Img_Downloader()
    with ThreadPoolExecutor(max_workers=5) as t:
        for idx in idx_array:
            t.submit(downloader.download_img, url_base.format(idx))

    t.shutdown()
