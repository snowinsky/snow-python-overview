vendor_batch_file_download_url = "https://jetpay-proxy-batch-runtime-ccb-api.prod.hccn/vendor/proxy/batch/file/download/response/{vendor_code}/{batch_name}"
vendor_batch_file_download_url_user = 'proxy'
vendor_batch_file_download_url_pasw = 'vendor'
vendor_batch_file_download_base_path = 'D:/doc/audit/202406'

import requests
import datetime
import time
import os

def downloadBatchResFile(vendor_code, batch_name):
    real_url = vendor_batch_file_download_url.format(vendor_code=vendor_code, batch_name=batch_name)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    res = requests.get(url=real_url, auth=(vendor_batch_file_download_url_user, vendor_batch_file_download_url_pasw), verify=False, headers=headers)
    if res.status_code == 200:
        file_folder = os.path.join(vendor_batch_file_download_base_path, datetime.date.today().strftime('%Y-%m-%d'))
        os.makedirs(file_folder, exist_ok=True)
        file_name = os.path.join(file_folder, batch_name + '.res')
        if os.path.exists(file_name):
            os.remove(file_name)
        with open(file_name, 'wb') as f:
            f.write(res.content)
            time.sleep(1)
        return file_name



if __name__ == '__main__':
    downloadBatchResFile('ccb', 'XXCCB2024052300000057-120138127')