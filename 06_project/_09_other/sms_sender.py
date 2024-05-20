import httplib2
from urllib import parse
class SmsSender(object):
    def send_sms(self, mobile, sms_info):
        """发送手机通知短信，用的是-互亿无线-的测试短信"""
        host = "106.ihuyi.com"
        sms_send_uri = "/webservice/sms.php?method=Submit"
        account = "C73152740" #api id
        pass_word = "af323101a456eb764ec4f797f0570e09" # api key
        params = parse.urlencode(
            {'account': account, 'password': pass_word, 'content': sms_info, 'mobile': mobile, 'format': 'json'}
        )
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib2.HTTPConnectionWithTimeout(host, port=80, timeout=30)
        conn.request("POST", sms_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
        return response_str.decode('utf8')


if __name__ == "__main__":
    res = SmsSender().send_sms("13920250489", "您的验证码是：1234。请不要把验证码泄露给其他人")
    print(res)
