
pab_bank_info = '''
PAB	15000107233280	22
'''

import requests


pab_request_url = 'https://ebank.sdb.com.cn:469/b2bi'
pab_company_code = '00901079800000223000'
pab_pri_cert_pwd = '21515960'
pab_cert_dn = 'CN=PAB@991120116636067462H@2000758181@YQ774167,OU=Enterprises,OU=PAB,O=PABCA,C=CN'

## 报502 连不上了
def get_bill(start, end, bank_acct):
    res = requests.post(pab_request_url, data='<xml><xml>')
    # res.encoding = res.apparent_encoding
    print(res.content.decode('gbk'))


if __name__ == '__main__':
    get_bill('20240511','20240511', '15000107233280')