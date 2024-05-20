
import requests
import re
import time

from splinter.browser import Browser
from urllib import parse


class Access12306(object):

    def __init__(self):
       self.browser = Browser(driver_name='chrome')

    # {'VAP': '北京北', 'BOP': '北京东', 'BJP': '北京', 'VNP': '北京南', 'IPP': '北京大兴', 'BXP': '北京......
    def station_names(self):
        """获取所有的车站信息，并返回map，key=code，value=name"""
        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9303'
        # 对网页发送get请求
        response = requests.get(url, verify=False)
        # 编写正则表达式
        stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
        station_map = {}
        for i in range(len(stations)):
            station_map[stations[i][0]] = stations[i][1]
        return station_map

    def login(self):
        """登录功能实现，手动识别验证码进行登录"""
        login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        init_my_url = 'https://kyfw.12306.cn/otn/view/index.html'

        self.browser.visit(login_url)
        time.sleep(1)
        # 选择登陆方式登陆
        print('请扫码登陆或者账号登陆……')
        while True:
            if self.browser.url != init_my_url:
                time.sleep(1)
            else:
                break

    def query_ticket(self, plan_date, station_src, station_tar, train_num=None):
        """买票功能实现"""
        ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        # 浏览器窗口最大化
        self.browser.driver.maximize_window()
        # 登陆
        self.login()
        # 跳转到抢票页面
        self.browser.visit(ticket_url)
        time.sleep(1)
        # 加载车票查询信息
        self.browser.cookies.add({"_jc_save_fromStation": self.__urlencode_station(station_src)})
        self.browser.cookies.add({"_jc_save_toStation": self.__urlencode_station(station_tar)})
        self.browser.cookies.add({"_jc_save_fromDate": plan_date})
        self.browser.reload()
        self.browser.find_by_text('查询').click()
        time.sleep(1)
        current_tr = self.browser.find_by_xpath('//tr[@datatran="' + train_num + '"]/preceding-sibling::tr[1]')
        current_time = current_tr.find_by_css('.start-t').text
        print(current_time)
        print(current_tr.find_by_tag('td'))


    def __urlencode_station(self, station_name):
        station_code = self.station_names()[station_name]
        st2uni = station_name.encode("unicode_escape")
        st2unicode_str = str(st2uni)
        st2unicode_str = st2unicode_str.removeprefix('b')
        st2unicode_str = st2unicode_str.removeprefix("'").removesuffix("'")
        st2unicode_str = st2unicode_str.replace('\\\\', '%')
        st2unicode_str = st2unicode_str + parse.quote("," + station_code)
        return st2unicode_str


if __name__ == '__main__':
    # st = '北京'
    # st2unicode = st.encode("unicode_escape")
    # st2unicodeString = str(st2unicode)
    # st2unicodeString = st2unicodeString.removeprefix('b')
    # st2unicodeString = st2unicodeString.removeprefix("'").removesuffix("'")
    # st2unicodeString = st2unicodeString.replace('\\\\', '%')
    # st2unicodeString = st2unicodeString + parse.quote(",BJ")
    # print(st2unicodeString)
    # st2unicodeString = parse.quote(st2unicodeString)
    # print(st2unicodeString)
    Access12306().query_ticket('2024-05-16', '天津南', '沧州西', 'G1230')