from ftplib import FTP

with FTP(host='168.33.48.98', user='jx020123', passwd='jx02012320101209', timeout=300, encoding='utf-8') as ftp:
    ftp.login()
    ftp.dir()
    ftp.cwd("batchpay")
    ftp.dir()

