from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import requests

# https://selenium-python-zh.readthedocs.io/en/latest/index.html
driver = webdriver.Chrome()  # 创建一个 Chrome WebDriver 实例
driver.get('https://image.baidu.com/')
search_input = driver.find_element(by=By.NAME, value="word")  # 获取到百度搜索框
search_input.send_keys("刘亦菲")  # 自动输入 刘亦菲
submit = driver.find_element(by=By.XPATH, value="//input[@type='submit' and @value='百度一下']")  # 获取到百度一下按钮
submit.click()

time.sleep(5)

imgs = driver.find_elements(by=By.XPATH, value="//img[contains(@class, 'main_img')]")
for img in imgs:
    img_src = img.get_attribute('src')
    print(img_src)
    if img_src.startswith("http"):
        res = requests.get(img_src)
        file_name = "{}.jpg".format(time.time())
        with open(file_name, 'wb', 1024) as f:
            f.write(res.content)
            time.sleep(1)
