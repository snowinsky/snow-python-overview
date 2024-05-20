# -*- coding: utf-8 -*-
from lxml import etree


class XPathXml(object):
    def __init__(self, xml_path):
        self.xml_path = xml_path

    def parse_by_xpath(self):
        html = etree.parse(self.xml_path, etree.HTMLParser())
        tr_list = html.xpath('html')
        for tr in tr_list:
            print(tr)



# etree.parse()


if __name__ == '__main__':
    XPathXml('D:/ws-py/tkinterdnd2/xpath.html').parse_by_xpath()
