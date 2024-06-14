# coding=utf-8
# pip install pycryptodome


import base64
import json

from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


# RSA加密类
# RSA 是个不对称加密。所以，用私钥加签，用公钥验签
class RSACrypt(object):

    def __init__(self, key):
        self.key = RSA.importKey(key)

    @staticmethod
    def dict2str(data_dict):
        tmp = []
        print("data_dict:", data_dict)
        for key in sorted(data_dict.keys()):
            value = data_dict[key]
            # print("value:",value)
            if isinstance(value, dict) or isinstance(value, list):
                tmp.append('{}={}'.format(key, json.dumps(value, sort_keys=True, separators=(',', ':'))))
            else:
                tmp.append('{}={}'.format(key, value))
        # print("tmp",tmp)
        return '&'.join(tmp)


# RSA公钥
class RSAPubCrypt(RSACrypt):

    # RSA公钥加密
    def encrypt(self, data, length=200):
        try:
            # 1024bit的证书用100，2048bit证书用200位
            data = data.encode('utf-8')
            cipher = PKCS1_v1_5.new(self.key)
            res = []
            for i in range(0, len(data), length):
                res.append(cipher.encrypt(data[i:i + length]))
            return str(base64.b64encode(b"".join(res)), encoding='utf-8')
        except:
            return False

    # RSA公钥验证签名
    def verify_sign(self, data, signature):
        try:
            if isinstance(data, dict):
                data = self.dict2str(data)
            data = data.encode('utf-8')
            h = SHA256.new(data)
            pkcs1_15.new(self.key).verify(h, base64.b64decode(signature))
            return True
        except (ValueError, TypeError):
            return False

    def verify_str_sign(self, data_str, sign_str):
        try:
            data = data_str.encode('utf-8')
            h = SHA256.new(data)
            pkcs1_15.new(self.key).verify(h, base64.b64decode(sign_str))
            return True
        except (ValueError, TypeError):
            return False


# RSA私钥
class RSAPrvCrypt(RSACrypt):

    # RSA私钥解密
    def decrypt(self, encrypt_data, length=256):
        # 1024bit的证书用128，2048bit证书用256位
        print("=====")
        try:
            cipher = PKCS1_v1_5.new(self.key)
            encrypt_data = base64.b64decode(encrypt_data)
            data = []
            for i in range(0, len(encrypt_data), length):
                data.append(cipher.decrypt(encrypt_data[i:i + length], 'xyz'))
            return str(b"".join(data), encoding='utf-8')
        except:
            return False

    # RSA私钥生成签名
    def sign(self, data):
        try:
            if isinstance(data, dict):
                data = self.dict2str(data)
            data = data.encode('utf-8')
            h = SHA256.new(data)
            signature = pkcs1_15.new(self.key).sign(h)
            return str(base64.b64encode(signature), encoding='utf-8')
        except:
            return False
