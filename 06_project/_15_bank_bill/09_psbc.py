

psbc_bank_acct = '''
912000010000021390
912003010000021389
912004010000021388
912006010000021873
912001010000022173
912009010000022175
912005010000022179
944000010000204287
944000010000204295
944002010000204285
944002010000204293
944004010000204291
944006010000204281
944030010000000187
944030010000000195
944032010000000193
944033010000000192
100475203890010001
912000010000001566
912001010000001979
912001010000003173
912002010000001564
912002010000001978
912002010000001986
912003010000001563
912003010000001977
912003010000001985
912004010000001562
912004010000001976
912005010000001561
912006010000001560
912006010000001982
912007010000001981
912000010000003174
912000010000003182
912001010000003181
912001010000019286
912002010000003180
912002010000003289
912003010000003296
912003010000019284
912004010000019283
912005010000003179
912006010000003178
912007010000003177
912008010000003176
912008010000003291
912009010000003183
912009010000003290
912000010000019303
912000010000019329
912000010000019923
912000010000019931
912000010000020087
912000010000020103
912001010000019302
912001010000020086
912002010000019327
912003010000019326
912004010000003295
912005010000003294
912005010000019332
912006010000003293
912007010000003292
912008010000019545
912002010000019913
912002010000019921
912002010000020085
912003010000003288
912003010000019920
912004010000019911
912004010000019929
912004010000020083
912005010000019928
912005010000020090
912007010000019546
912007010000019918
912007010000019934
912007010000020080
912007010000020106
912007010000020114
912008010000019909
912008010000019933
912008010000020105
912008010000020113
912009010000019916
912009010000020088
912009010000020104
912009010000020112
912002010000019301
912006010000021055
912005010000021056
912003010000021058
912002010000021059
912007010000021062
912006010000021063
912005010000021064
912003010000021066
912002010000021067
912001010000021068
912004010000021081
912003010000021082
912002010000021083
912001010000021084
912000010000021085
912009010000021086
912008010000021087
912006010000021089
912003010000021090
912002010000021091
942005010028946684
912006010000021386
912007010000021385
912008010000021384
912009010000021383
912000010000021382
912001010000021381
912005010000021379
912006010000021378
912007010000021377
912008010000021376
912007010000021393
912008010000021392
912009010000021391
912001010000021399
912008010000021400
912007010000021401
912006010000021402
912003010000021868
912002010000021869
912009010000021870
912005010000021874
912003010000021876
912001010000021878
912007010000021880
912006010000021881
912005010000021882
912004010000021883
912002010000021885
912008010000022044
912007010000022045
912006010000022046
912005010000022047
912004010000022048
912003010000022049
912009010000022050
912008010000022051
912007010000022052
912000010000022166
912008010000022168
912004010000022170
912003010000022171
912008010000022176
912009010000024361
'''

req_xml_demo = '''
<?xml version="1.0" encoding="GBK" standalone="yes"?>
<root>
    <Head>
        <OpName>2108</OpName>
        <Outsys_Code>1216004</Outsys_Code>
        <OpDate>20240625</OpDate>
        <merch_id>120020160004</merch_id>
    </Head>
    <Param>
        <Query_Account>2342332453534532454</Query_Account>
        <Begin_Date>20240624</Begin_Date>
        <End_Date>20240624</End_Date>
    </Param>
</root>
'''

from socket import *  # 导入 socket 模块
import datetime
import xml.etree.ElementTree as ET

ADDR = ('10.25.2.21', 9331)
# ADDR = ('192.168.249.76', 10047)
psbc_outcode = '1216004'
psbc_merch_id = '120020160004'
CHARSET = 'GBK'
def get_bill(start_date, end_date, credit_bank_account):
    with socket(AF_INET, SOCK_STREAM) as tcpCliSock:
        tcpCliSock.connect(ADDR)
        tcpCliSock.settimeout(300)

        now = datetime.datetime.now()
        reqDate = now.strftime('%Y%m%d')
        reqTime = now.strftime('%H%M%S')
        req_xml = f'''
        <?xml version="1.0" encoding="GBK" standalone="yes"?>
        <root>
            <Head>
                <OpName>2108</OpName>
                <Outsys_Code>{psbc_outcode}</Outsys_Code>
                <OpDate>{reqDate}</OpDate>
                <merch_id>{psbc_merch_id}</merch_id>
            </Head>
            <Param>
                <Query_Account>{credit_bank_account}</Query_Account>
                <Begin_Date>{start_date}</Begin_Date>
                <End_Date>{end_date}</End_Date>
            </Param>
        </root>
        '''
        # 把xml合并成一行
        req_xml = ''.join([a.strip() for a in req_xml.split('\n')])
        # 前面加xml字符串的长度，格式是0+长度（左对齐，补空格，7位）
        req_data = (str(len(req_xml))).rjust(5, '0')+'00000' + req_xml
        print(req_data)
        tcpCliSock.send(req_data.encode(CHARSET))
        res_data_length = tcpCliSock.recv(6)
        if res_data_length:
            res_data = tcpCliSock.recv(int(res_data_length))
            print('response=', res_data.decode(CHARSET))
            # xml_root = ET.fromstring(res_data.decode(CHARSET))
            # respCode = xml_root.find('RespCode').text
            # respSeqNo = xml_root.find('RespSeqNo').text
            # if respCode == '0000':
            #     return respSeqNo, respCode, xml_root.find('FileFlag').text, xml_root.findall('./Cmp/BatchFileName')[
            #         0].text
            # else:
            #     return respSeqNo, respCode, None, []
        tcpCliSock.close()
# 能ping通，但是连接不上，报timeout
if __name__ == '__main__':
    bank_acct_list = list(filter(lambda a:len(a) > 1, psbc_bank_acct.split('\n')))
    get_bill('20240707','20240707', '912008010000019545')
    # for ba in bank_acct_list:
    #     print(ba)
    #     get_bill('20231015','20231015', ba)