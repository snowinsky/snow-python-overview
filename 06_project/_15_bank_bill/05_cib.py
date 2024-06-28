import requests
import datetime
import xml.etree.ElementTree as ET

cib_front_machine_address = 'http://10.64.2.197:8007'
cib_customer_id = '0820929017'
cib_op_username = 'qianzhi'
cib_op_pwd = 'a21515960'


banc_acct_list = (
    '441270100100532685',
    '441270100100532815',
    '441270100100532933',
    '441270100100533098',
    '441270100100533123',
    '441270100100533245',
    '441270100100532567',
    '441270100100533369',
    '441270100100533483',
    '441270100100533504',
    '441270100100533613',
    '441270100100533859',
    '441270100100533977',
    '441270100100534141',
    '441270100100550517',
    '441270100100550638',
    '441270100100550750'
)


def get_bill(start_date, end_date, bank_acct):
    '''

    :param start_date: yyyy-MM-dd
    :param end_date: yyyy-MM-dd
    :param bank_acct: 441270100100550750
    :return:
    '''
    req_xml = f'''
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <FOX>
    	<SIGNONMSGSRQV1>
    		<SONRQ>
    			<DTCLIENT>
    				{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    			</DTCLIENT>
    			<CID>
    				{cib_customer_id}
    			</CID>
    			<USERID>
    				{cib_op_username}
    			</USERID>
    			<USERPASS>
    				{cib_op_pwd}
    			</USERPASS>
    			<GENUSERKEY>
    				N
    			</GENUSERKEY>
    		</SONRQ>
    	</SIGNONMSGSRQV1>
    	<SECURITIES_MSGSRQV1>
    		<SCUSTSTMTTRNRQ>
    			<TRNUID>
    				00000000001
    			</TRNUID>
    			<SCUSTSTMTRQ>
    				<ACCTFROM>
    					<ACCTID>
    						{bank_acct}
    					</ACCTID>
    				</ACCTFROM>
    				<INCTRAN>
    					<DTSTART>
    						{start_date}
    					</DTSTART>
    					<DTEND>
    						{end_date}
    					</DTEND>
    					<PAGE>
    						1
    					</PAGE>
    				</INCTRAN>
    			</SCUSTSTMTRQ>
    		</SCUSTSTMTTRNRQ>
    	</SECURITIES_MSGSRQV1>
    </FOX>
    '''
    req_data = ''.join(a.strip() for a in req_xml.split("\n"))
    res = requests.post(url=cib_front_machine_address, data=req_data)
    print("##########################", bank_acct, "\n\n")
    print(res.text)
    res_xml_root = ET.fromstring(res.text)
    res_code = res_xml_root.findall("./SIGNONMSGSRSV1/SONRS/STATUS/CODE")[0].text
    if res_code == '0':
        res_tran_code = res_xml_root.findall("./SECURITIES_MSGSRSV1/SCUSTSTMTTRNRS/STATUS/CODE")[0].text
        if res_tran_code == '0':
            tran_list = res_xml_root.findall("./SECURITIES_MSGSRSV1/SCUSTSTMTTRNRS/SCUSTSTMTRS/TRANLIST/STMTTRN")
            tran_dic_list = []
            for tran in tran_list:
                tran_dic = {}
                for a in tran.iter():
                    tran_dic[a.tag] = a.text
                tran_dic_list.append(tran_dic)
            print(res_code, res_tran_code, tran_dic_list)

        else:
            res_tran_msg = res_xml_root.findall("./SECURITIES_MSGSRSV1/SCUSTSTMTTRNRS/STATUS/MESSAGE")[0].text
            print(res_code, res_tran_code, res_tran_msg, "#######", bank_acct)


res_xml = '''
<FOX>
    <SIGNONMSGSRSV1>
        <SONRS>
            <STATUS>
                <CODE>0</CODE>
                <SEVERITY>INFO</SEVERITY>
            </STATUS>
            <DTSERVER>2024-06-14 11:36:11</DTSERVER>
        </SONRS>
    </SIGNONMSGSRSV1>
    <SECURITIES_MSGSRSV1>
        <SCUSTSTMTTRNRS>
            <TRNUID>00000000001</TRNUID>
            <STATUS>
                <CODE>0</CODE>
                <SEVERITY>INFO</SEVERITY>
            </STATUS>
            <SCUSTSTMTRS>
                <CURDEF>RMB</CURDEF>
                <ACCTFROM>
                    <ACCTID>441270100100532815</ACCTID>
                    <NAME>捷信消费金融有限公司</NAME>
                </ACCTFROM>
                <TRANLIST MORE="N">
                    <DTSTART>2024-05-11</DTSTART>
                    <DTEND>2024-05-11</DTEND>
                    <STMTTRN>
                        <SRVRTID>99990172</SRVRTID>
                        <TRNTYPE>CREDIT</TRNTYPE>
                        <TRNCODE>232</TRNCODE>
                        <DTACCT>2024-05-11T08:00:00</DTACCT>
                        <TRNAMT>2841.39</TRNAMT>
                        <BALAMT>177455.96</BALAMT>
                        <CURRENCY>RMB</CURRENCY>
                        <MEMO>中心归集|资金归集</MEMO>
                        <CORRELATE_ACCTID>441270100100533369</CORRELATE_ACCTID>
                        <CORRELATE_NAME>捷信消费金融有限公司</CORRELATE_NAME>
                        <CHEQUENUM>99</CHEQUENUM>
                        <BILLTYPE></BILLTYPE>
                        <BILLNUMBER></BILLNUMBER>
                        <CORRELATE_BANKNAME>兴业银行</CORRELATE_BANKNAME>
                        <CORRELATE_BANKCODE>44127</CORRELATE_BANKCODE>
                        <BUSINESSTYPE></BUSINESSTYPE>
                        <ATTACHINFO>2024051100499891481000002</ATTACHINFO>
                    </STMTTRN>
                </TRANLIST>
                <LEDGERBAL>
                    <BALAMT>58993.44</BALAMT>
                    <DTASOF>2024-06-14</DTASOF>
                </LEDGERBAL>
                <AVAILBAL>
                    <BALAMT>58993.44</BALAMT>
                    <DTASOF>2024-06-14</DTASOF>
                </AVAILBAL>
            </SCUSTSTMTRS>
        </SCUSTSTMTTRNRS>
    </SECURITIES_MSGSRSV1>
</FOX>
'''

if __name__ == '__main__':
    for ba in banc_acct_list:
        get_bill('2024-05-11', '2024-05-11', ba)
        break
