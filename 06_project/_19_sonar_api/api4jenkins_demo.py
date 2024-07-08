from api4jenkins import Jenkins

if __name__ == '__main__':
    j = Jenkins('https://jenkins.homecreditcfc.cn/job/ddap', auth=('jack.ji', 'In@202406'))
    print(j)
    print(j.version)
    print(j.get_job('ddap-online-abc'))


