# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：abc_socket_client.py

from socket import *  # 导入 socket 模块
import datetime
import xml.etree.ElementTree as ET
import requests

master = {
    'host': '10.25.2.224',
    'port': 3837,
    'url': 'http://10.25.2.224:8082/abc/file/',
    'corpNo' : "02999953200004054",
    'opNo' : "0003"
}

slaver = {
    'host': '10.31.2.207',
    'port': 3837,
    'url': 'http://10.31.2.207:8081/abc/file/',
    'corpNo' : "6612502044205888",
    'opNo' : "0020"
}

HOST = slaver['host']  # or 'localhost'
PORT = slaver['port']
abcFileServiceUrl = slaver['url']



BUFSIZ = 1024
ADDR = (HOST, PORT)
CHARSET = 'GB18030'

corpNo = master['corpNo']
opNo = master['opNo']

creditBankAccounts = (
    "190001040023069", "190001040018796", "190001040018804", "190001040018812", "190001040018846", "190001040018838",
    "190001040018853", "190001040018861", "190001040018879", "190001040018887", "190001040018911", "190001040018903",
    "190001040018895", "190001040018945", "190001040018937", "190001040018952", "190001040019000", "190001040019034",
    "190001040019026", "190001040019083", "190001040019075", "190001040019067", "190001040019059", "190001040020693",
    "190001040020719", "190001040023077")




def get_bill_name_abc_socket_client(startDate, endDate, creditBankAccount):
    with socket(AF_INET, SOCK_STREAM) as tcpCliSock:
        tcpCliSock.connect(ADDR)
        tcpCliSock.settimeout(300)

        now = datetime.datetime.now()
        reqDate = now.strftime('%Y%m%d')
        reqTime = now.strftime('%H%M%S')
        req_xml = f'''
        <?xml version="1.0" encoding="GB18030" standalone="yes"?>
        <ap>
            <CCTransCode>
                CQRA18
            </CCTransCode>
            <ProductID>
                ICC
            </ProductID>
            <ChannelType>
                ERP
            </ChannelType>
            <CorpNo>
                {corpNo}
            </CorpNo>
            <OpNo>
                {opNo}
            </OpNo>
            <AuthNo>
            </AuthNo>
            <ReqDate>
                {reqDate}
            </ReqDate>
            <ReqTime>
                {reqTime}
            </ReqTime>
            <Sign>
            </Sign>
            <Corp>
                <StartDate>
                    {startDate}
                </StartDate>
                <EndDate>
                    {endDate}
                </EndDate>
            </Corp>
            <Cmp>
                <DbAccNo>
                    {creditBankAccount}
                </DbAccNo>
                <DbProv>
                    02
                </DbProv>
                <DbCur>
                    01
                </DbCur>
            </Cmp>
        </ap>
        '''
        # 把xml合并成一行
        req_xml = ''.join([a.strip() for a in req_xml.split('\n')])
        # 前面加xml字符串的长度，格式是0+长度（左对齐，补空格，7位）
        req_data = ('0' + str(len(req_xml))).ljust(7, ' ') + req_xml
        tcpCliSock.send(req_data.encode(CHARSET))
        res_data_length = tcpCliSock.recv(7)
        if res_data_length:
            res_data = tcpCliSock.recv(int(res_data_length))
            # print('response=', res_data.decode(CHARSET))
            xml_root = ET.fromstring(res_data.decode(CHARSET))
            respCode = xml_root.find('RespCode').text
            respSeqNo = xml_root.find('RespSeqNo').text
            if respCode == '0000':
                return respSeqNo, respCode, xml_root.find('FileFlag').text, xml_root.findall('./Cmp/BatchFileName')[
                    0].text
            else:
                return respSeqNo, respCode, None, []
        tcpCliSock.close()


def get_bill_content(bill_file_name):
    res = requests.get(abcFileServiceUrl + bill_file_name)
    res.encoding = CHARSET
    return res.text

def get_all_bill_for_all_accts(recon_date):
    for credit_bank_acct in creditBankAccounts:
        seqNo, rescode, fileflag, filename = get_bill_name_abc_socket_client(recon_date, recon_date, credit_bank_acct)
        print(seqNo, rescode, fileflag, filename)
        if rescode == '0000' and fileflag == '1':
            print("############", filename, "##########")
            print("file content====", get_bill_content(filename))

def get_bill_for_acct(recon_date, bank_acct):
    seqNo, rescode, fileflag, filename = get_bill_name_abc_socket_client(recon_date, recon_date, bank_acct)
    print(seqNo, rescode, fileflag, filename)
    if rescode == '0000' and fileflag == '1':
        print("############", filename, "##########")
        print("file content====", get_bill_content(filename))

if __name__ == '__main__':
    get_all_bill_for_all_accts('20240715')
    # get_bill_for_acct('20240715', '190001040020693')

