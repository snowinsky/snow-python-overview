#!/usr/bin/env python3
# coding: utf-8
import paramiko
from paramiko.sftp_client import SFTPClient


class SimpleSftp(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.timeout = 300
        self.sftp_client = None

    def login(self, user, password):
        t = paramiko.Transport((self.host, int(self.port)))
        t.banner_timeout = self.timeout
        t.connect(username=user, password=password)
        sftp_client = paramiko.SFTPClient.from_transport(t)
        self.sftp_client = sftp_client
        return sftp_client

    def listdir(self, path):
        return self.sftp_client.listdir(path)

    def upload(self, local_path, server_path):
        return self.sftp_client.put(localpath=local_path, remotepath=server_path)

    def download(self, local_path, server_path):
        self.sftp_client.get(remotepath=server_path, localpath=local_path)


if __name__ == '__main__':
    simple_sftp = SimpleSftp('sftpdmz2c.homecreditcfc.cn', 22)
    simple_sftp.login('hc_icbc', '3nDagqdKl9YYXfk2429N')
    fl = simple_sftp.listdir("./hc_icbc/")
    print(fl)
    print(sorted(fl, reverse=True))
    #print(simple_sftp.listdir("./hc_icbc/dd_res/ICBC20240603500026.TXT"))

    simple_sftp.download('D:/data/aaa.TXT', "./hc_icbc/dd_res/ICBC20240603500026.TXT")

