import requests
import os

baofu_url = 'https://public.baofoo.com/cutpayment/protocol/backTransRequest'

verify_file =  'D:/doc/vendor对账/baofu/baofu_https_base64_x509.cer'
cert_file = 'D:/doc/vendor对账/baofu/baofu_https_base64_x509_20240624.cer'

cert_file1 = 'D:/doc/vendor对账/baofu/baofu_https_base64_x509_20240624.crt'

if __name__ == '__main__':
    res = requests.get(baofu_url, cert=os.path.join(cert_file1))
    print(res.text)