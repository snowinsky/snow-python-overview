ghb_request_url = 'http://10.67.0.115:8081/ghbankgayway4ent/rest/gayway'
ghb_custNo = '5000011456'

bank_acct_list = ('805880100016516')

import datetime
import requests


def get_bill(start_date, end_date, bank_acct):
    req_xml = f'''
        <ROOT>
            <TRNCD>ZTSA63Q03</TRNCD>
            <CUSTNO>{ghb_custNo}</CUSTNO>
            <ENTWORKDT>{datetime.datetime.now().strftime('%Y%m%d')}</ENTWORKDT>
            <ENTSEQNO>{datetime.datetime.now().strftime('%H%M%S')}</ENTSEQNO>
            <ACCTNO>{bank_acct}</ACCTNO>
            <BGNDT>{start_date}</BGNDT>
            <ENDDT>{end_date}</ENDDT>
            <BGNROWNO>1</BGNROWNO>
            <RQROWNUM>1000</RQROWNUM>
        </ROOT>
        '''
    req_data = ''.join([a.strip() for a in req_xml.split('\n')])
    res = requests.post(ghb_request_url, data=req_data)
    print(res.text)


## 连不上
if __name__ == '__main__':
    for ba in bank_acct_list:
        get_bill('20240511', '20240511', ba)
