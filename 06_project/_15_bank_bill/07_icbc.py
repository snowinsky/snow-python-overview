import uuid
from base64 import b64decode

icbc_request_url = 'https://gw.open.icbc.com.cn/api/mybank/enterprise/trade/qhisd/V1'
icbc_appid = '10000000000003186530'
icbc_private_key = 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDWIVxCO6D+NoZeeBQUnXAk8iFSbIXTMKz1jXX5sUOWO1dSjfaN7cmwsg2F9pUxLaY1WM2MRnKC9mi32hqpGojN7aKqVHkAYxDslyQBZeQ9RhGnzBq/+zHwXxm1TZ3rsJsUPHyA7FquRTX01A/PD5kXOeC68EQRmHbJ/C6O2ZfmUbX/Bp12ugcSmDXeH9wABEF1FimvSG9BcG0DHQ4XZHGMx/ODZ5ho2g0sFx+BTZ4LaZJu6JxJ5oKyXGEd0lt61HUXwCCAXX2IgCyjKXIzudsCtAQwGEkT0onsE+9QORxvpMjltudZmOFQT2S9+nBHWv1UPr4UlScjmPy3ivus4pUbAgMBAAECggEAWBBmShMN9h7kiiumToglW/x8udJKA34sU9y23VcK7dk/44LhGKPn5BSGPUcZOp2EksIP3xYF+Fhw3tQDTPLNuqt1z8ln7kHP7w2F0FFgWdbcYf8uLTCY7DugbhEa1pjOXrc1mSwbazqpoyQn0Eeg9Y1nIFq6E+Z5TD67wyI4N484EaPEg5pU7smtNoHDyRms9mrY/E/zjiRVYJGq/PaDQnKo1qwDUyqBldD3AHE8h5reuA3yF1/G4wCqhT+a3p679d7FsdVqYKytsRO9Kufdsk1gG5L0lJyeAQPmtZRxq+QbWw9Ux6uhynT2KrGQlS7/1Uoqw9H1yvG89FauGBFrmQKBgQD/hlsxt2PnFEx26T0bljTNZpn+AY0+12nH0+yDAO3D+mMZuC+vT2HyvGlq47/WqNpM2KHctnU8MTulOn/Mprjqe1WZp/be/x/0NoKEc+BYZRQ7fPzzLjLEjNF6lKoPUaYKZRmtQ4+6GYd8IHwBJIMOV0cQ0imt/xQhN4tVf2AeNQKBgQDWh0xQ2HNdQSCsI6d4wva+/ExTRjtgJnolS2OIaa4xGcn2wnZvnkDFK2RfgmWQhDeB0IzELfA+DaLhWVWKB6g2BoLw1mBxjZyHgdj4r1xb0JIhpiagkKJNFU8XSV9IiJfqklS4d3ZlHJjjNtA6eNU+1dERHLmM8mlydfGWhJeQDwKBgBJRNVRZCyZThC+6BJFnsR1QT5Wv0spAcurKPFgfxuuXlWcQlwqALEtUSlJJRUVEEXIUzXWe9sR72wS7LtIi2XqloLtFGSNfMpE1HyITlG+Bv3OMQC3GkAka9yFMauxyM+7m1HJhN3plvhqd0YXbcjGi/AsupaI9eNnwu2JDoUZJAoGAG5uZ1KWmYw/oln6YJNBiVL2/TNAy//KzsWz8SCfhhOwes6Te/QpOp5En/6qWS3zYb9pY4z5ONo4msf1/Jp5JpXo9C6VrD/H7fOzW8VoP9rjmtXHecrdqS6U8YnDM1FbPxh5CzOKC2AxQGJ2LOpsmRknZ9+vMbTkdHN/U0VwK7T0CgYEAgG10GZUfcPJBea+3Kr2wu4ujLzUwU2bZrsQPK8Pc2dn9Deh0hIXTYOpBFajq9669JeEXRA0UZL8KqcqLpKYQ4B3aUoFVD3PMfNX3G2VERWj51G+LPQcaErDR8qzbnybnezyBzl1x98nbRJVvzLiiKnAffnI6Gmc5X/Y1wO5e4gs='
icbc_public_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCMpjaWjngB4E3ATh+G1DVAmQnIpiPEFAEDqRfNGAVvvH35yDetqewKi0l7OEceTMN1C6NPym3zStvSoQayjYV+eIcZERkx31KhtFu9clZKgRTyPjdKMIth/wBtPKjL/5+PYalLdomM4ONthrPgnkN4x4R0+D4+EBpXo8gNiAFsNwIDAQAB'
icbc_sign_type = 'RSA2'

bank_acct_list = (
    '0302035119300370994', '0302035119300371001', '0302035119300379538', '0302035119300379662', '0302035119300379786',
    '0302035119300379813', '0302035119300379937', '0302035119300380927', '0302035119300380005', '0302035119300380129',
    '0302035119300380253', '0302035119300380377', '0302035119300380404', '0302035119300380528', '0302035119300380652',
    '0302035119300380776', '0302035119300380803', '0302035119300387915', '0302035119300388019', '0302035119300388267',
    '0302035119300392362', '0302035119300391983', '0302035119300392087', '0302035119300392238', '0302035119300392114',
    '0302035119300414280', '4000040419200195366', '0302035119300388143'
)

import datetime
import json
import requests
from rsa_crypt.rsa_crypt import RSAPubCrypt, RSAPrvCrypt, RSACrypt
import urllib.parse


def get_bill(start_date, end_date, bank_acct):
    req_dic_biz = {
        'trans_code': 'QHISD',
        'tran_date': datetime.datetime.now().strftime('%Y%m%d'),
        'tran_time': datetime.datetime.now().strftime('%H:%M:%S.%f'),
        'next_tag': '',
        'f_seq_no': '00000001',
        'account_no': bank_acct,
        'bank_code': '',
        'begin_date': start_date,
        'end_date': end_date,
        'currency': 'CNY'
    }

    biz_content = json.dumps(req_dic_biz)
    msg_id = str(uuid.uuid1()).replace('-', '')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    req_dic = {
        'app_id': icbc_appid,
        'sign_type': icbc_sign_type,
        'charset': 'utf-8',
        'format': 'json',
        # 'ca': '',
        # 'app_auth_token': '',
        'msg_id': msg_id,
        'timestamp': timestamp,
        'biz_content': biz_content
    }

    sign_url = icbc_request_url[icbc_request_url.index('/', 10):]
    rsa_private_key = RSAPrvCrypt(b64decode(icbc_private_key))
    sign_str = sign_url + '?' + rsa_private_key.dict2str(req_dic)
    signed_str = rsa_private_key.sign(sign_str)

    req_dic['sign'] = signed_str

    header = {
        'APIGW-VERSION': 'v2_20190522',
        'Content-Type': 'application/x-www-form-urlencoded',
        'charset': 'UTF-8'
    }
    res = requests.post(icbc_request_url + '?' + urllib.parse.urlencode(req_dic), headers=header)
    res_json = res.text
    print("res_text=", res_json)
    res_data = json.loads(res_json)
    res_biz_content = res_json[24:res_json.index(',"sign":"')]
    print('res_biz_content_text=', res_biz_content)
    res_sign = res_data['sign']
    print('res_sign_text=', res_sign)
    rsa_public_key = RSAPubCrypt(b64decode(icbc_public_key))
    print(rsa_public_key)
    print(rsa_public_key.verify_str_sign(res_biz_content, res_sign))



## 需要验签，总是不对
if __name__ == '__main__':
    for ba in bank_acct_list:
        if(ba == '0302035119300379662'):
            get_bill('20240511', '20240511', ba)
            break
        # break
