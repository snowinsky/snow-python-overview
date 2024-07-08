import csv

import requests
import json


def get_git_url_from_sonar(name_space, project_name):
    url = f"http://sonarqube.prod.hccn/api/project_links/search?projectKey=it-dev:{name_space}:{project_name}"
    headers = {
        'Authorization': 'Basic amFjay5qaTpJbkAyMDI0MDY='
    }
    response = requests.request("GET", url, headers=headers)
    res_text_json = response.text
    res_json = json.loads(res_text_json)
    try:
        return list(filter(lambda x: x['type'] == 'scm', res_json['links']))[0]['url']
    except Exception as e:
        print("get_git_url_from_sonar", name_space, project_name, e)
        return ''


def get_issue_count_from_sonar(name_space, project_name):
    metricKeys = ','.join(
        "violations,blocker_violations,critical_violations,major_violations,info_violations,minor_violations".split(
            ','))
    url = f"http://sonarqube.prod.hccn/api/measures/component?component=it-dev:{name_space}:{project_name}&metricKeys={metricKeys}"
    headers = {
        'Authorization': 'Basic amFjay5qaTpJbkAyMDI0MDY='
    }
    response = requests.request("GET", url, headers=headers)
    res_text_json = response.text
    res_json = json.loads(res_text_json)

    fake_return = [{'metric': 'major_violations', 'value': '-1', 'bestValue': False},
                   {'metric': 'minor_violations', 'value': '-1', 'bestValue': False},
                   {'metric': 'critical_violations', 'value': '-1', 'bestValue': False},
                   {'metric': 'blocker_violations', 'value': '-1', 'bestValue': False},
                   {'metric': 'info_violations', 'value': '-1', 'bestValue': True},
                   {'metric': 'violations', 'value': '-1', 'bestValue': False}]
    try:
        l = res_json['component']['measures']
        if l == None or len(l) == 0:
            return fake_return
        else:
            return l
    except Exception as e:
        print("get_issue_count_from_sonar", name_space, project_name, e)
        return fake_return


def get_sonar_report_url(name_space, project_name):
    return f"http://sonarqube.prod.hccn/project/extension/dependencycheck/report_page?id=it-dev:{name_space}:{project_name}&qualifier=TRK"


def get_projects(name_space):
    def get_projects_by_page(name_space, page):
        url = f"http://sonarqube.prod.hccn/api/projects/search?p={page}&qualifiers=TRK&q=it-dev:{name_space}"
        headers = {
            'Authorization': 'Basic MGI1NWU3N2IyZDMwMWQ0NzczZTYzMTBjNWQzYjU0M2RjOTgyNjdkMDo='
        }
        response = requests.request("GET", url, headers=headers)
        res_json = json.loads(response.text)
        if len(res_json['components']) == 0:
            return []
        project_name_list = [a['key'] for a in res_json['components']]
        return project_name_list

    project_key_list = []
    page = 1
    while (True):
        l = get_projects_by_page(name_space, page)
        if len(l) == 0:
            return project_key_list
        else:
            project_key_list = project_key_list + l
            page = page + 1


name_space_list = ('dddt', 'bank-vendor', 'ddap', 'instant-payment', 'hs4repayment')


def write_sonar_scan_status_to_txt():
    with open("D://doc/payment_project_sonar_reports_summary_v01.txt", 'w') as f:
        f.write(','.join(
            ["project_name", 'git_url', 'blocker', 'critical', 'major', 'minor', 'info', 'report_url', 'author']))
        f.write('\n')
        for ns in name_space_list:
            project_name_list = sorted(get_projects(ns))
            for project_name in project_name_list:
                name_space = project_name.split(":")[1]
                proj_name = project_name.split(":")[2]
                print(project_name)
                git_url = get_git_url_from_sonar(name_space, proj_name)
                issues = get_issue_count_from_sonar(name_space, proj_name)
                print(project_name, issues)
                blocker = list(filter(lambda x: x['metric'] == 'blocker_violations', issues))[0]['value']
                critical = list(filter(lambda x: x['metric'] == 'critical_violations', issues))[0]['value']
                major = list(filter(lambda x: x['metric'] == 'major_violations', issues))[0]['value']
                minor = list(filter(lambda x: x['metric'] == 'minor_violations', issues))[0]['value']
                info = list(filter(lambda x: x['metric'] == 'info_violations', issues))[0]['value']
                report_url = get_sonar_report_url(name_space, proj_name)
                f.write(','.join([project_name, git_url, blocker, critical, major, minor, info, report_url, 'jack.ji']))
                f.write('\n')


def write_sonar_scan_status_to_csv():
    with open("D://doc/payment_project_sonar_reports_summary_v01.csv", 'w', newline='') as f:
        header = ["project_name", 'git_url', 'blocker', 'critical', 'major', 'minor', 'info', 'report_url', 'author',
                  'report_check']
        csv_w = csv.DictWriter(f, header)
        csv_w.writeheader()
        for ns in name_space_list:
            project_name_list = sorted(get_projects(ns))
            for project_name in project_name_list:
                name_space = project_name.split(":")[1]
                proj_name = project_name.split(":")[2]
                print(project_name)
                git_url = get_git_url_from_sonar(name_space, proj_name)
                issues = get_issue_count_from_sonar(name_space, proj_name)
                print(project_name, issues)
                blocker = list(filter(lambda x: x['metric'] == 'blocker_violations', issues))[0]['value']
                critical = list(filter(lambda x: x['metric'] == 'critical_violations', issues))[0]['value']
                major = list(filter(lambda x: x['metric'] == 'major_violations', issues))[0]['value']
                minor = list(filter(lambda x: x['metric'] == 'minor_violations', issues))[0]['value']
                info = list(filter(lambda x: x['metric'] == 'info_violations', issues))[0]['value']
                report_url = get_sonar_report_url(name_space, proj_name)
                report_check = check_sonar_report(name_space, proj_name)
                csv_w.writerow({
                    "project_name": project_name, 'git_url': git_url, 'blocker': blocker, 'critical': critical,
                    'major': major, 'minor': minor, 'info': info, 'report_url': report_url, 'author': 'jack.ji',
                    'report_check': report_check
                })

def write_sonar_scan_status_to_csv(project_key_list):
    with open("D://doc/payment_project_sonar_reports_summary_v01.csv", 'w', newline='') as f:
        header = ["project_name", 'git_url', 'blocker', 'critical', 'major', 'minor', 'info', 'report_url', 'author',
                  'report_check']
        csv_w = csv.DictWriter(f, header)
        csv_w.writeheader()
        for project_name in project_key_list:
            name_space = project_name.split(":")[1]
            proj_name = project_name.split(":")[2]
            print(project_name)
            git_url = get_git_url_from_sonar(name_space, proj_name)
            issues = get_issue_count_from_sonar(name_space, proj_name)
            print(project_name, issues)
            blocker = list(filter(lambda x: x['metric'] == 'blocker_violations', issues))[0]['value']
            critical = list(filter(lambda x: x['metric'] == 'critical_violations', issues))[0]['value']
            major = list(filter(lambda x: x['metric'] == 'major_violations', issues))[0]['value']
            minor = list(filter(lambda x: x['metric'] == 'minor_violations', issues))[0]['value']
            info = list(filter(lambda x: x['metric'] == 'info_violations', issues))[0]['value']
            report_url = get_sonar_report_url(name_space, proj_name)
            report_check = check_sonar_report(name_space, proj_name)
            csv_w.writerow({
                "project_name": project_name, 'git_url': git_url, 'blocker': blocker, 'critical': critical,
                'major': major, 'minor': minor, 'info': info, 'report_url': report_url, 'author': 'jack.ji',
                'report_check': report_check
            })


project_key_scope = '''
it-dev:dddt:WAPPAY
it-dev:dddt:al-alipay-repay-monitor
it-dev:dddt:al-dd-monitor
it-dev:dddt:al-offline-payment
it-dev:dddt:al-repayment-service
it-dev:dddt:bas-be
it-dev:dddt:bas-rest
it-dev:dddt:cashier-boss-monitor-ws
it-dev:dddt:commission-report
it-dev:dddt:customer-common-api
it-dev:dddt:dd-batch-recover
it-dev:dddt:dd-router-api
it-dev:dddt:dd-router-job
it-dev:dddt:ddrs
it-dev:dddt:dds
it-dev:dddt:dds-ddme
it-dev:dddt:dds-monitor-ws
it-dev:dddt:dds-mpf
it-dev:dddt:dds-plum
it-dev:dddt:dds-report
it-dev:dddt:dds-summary-api
it-dev:dddt:dps-alipay
it-dev:dddt:hackthonaiops
it-dev:dddt:hcc-huigou-api
it-dev:dddt:jetpay-abnormal-routing
it-dev:dddt:jetpay-abnormal-routing-fast
it-dev:dddt:jetpay-al-bff
it-dev:dddt:jetpay-al-dd-evaluate
it-dev:dddt:jetpay-al-dd-life-cycle
it-dev:dddt:jetpay-al-dd-router-api
it-dev:dddt:jetpay-al-gateway
it-dev:dddt:jetpay-boss-adr
it-dev:dddt:jetpay-boss-adr-lib
it-dev:dddt:jetpay-boss-dd-life-cycle
it-dev:dddt:jetpay-boss-dd-search-result
it-dev:dddt:jetpay-dd-cancel-auth
it-dev:dddt:jetpay-dd-router-api
it-dev:dddt:jetpay-dd-router-job
it-dev:dddt:jetpay-hsw-ssdd-normal-ws
it-dev:dddt:jetpay-joss
it-dev:dddt:jetpay-monitor
it-dev:dddt:jetpay-monitor-regist-center
it-dev:dddt:jetpay-monitor-ssdd
it-dev:dddt:jetpay-search-result-fast
it-dev:dddt:joss-bill-export
it-dev:dddt:joss-customer-license
it-dev:dddt:joss-router
it-dev:dddt:no-cashier-alipay
it-dev:dddt:no-cashier-baofu
it-dev:dddt:no-cashier-front
it-dev:dddt:no-cashier-wechat
it-dev:dddt:no-jetcollect-dd-result
it-dev:dddt:no-jetpay-dd-life-cycle
it-dev:dddt:no-payment-activity
it-dev:dddt:no-payment-order
it-dev:dddt:no-pg-jetcollect-abnormal
it-dev:dddt:no-wappay
it-dev:dddt:payment-activity
it-dev:dddt:payment-monitor
it-dev:dddt:payment-order
it-dev:dddt:payment-to-zsamc
it-dev:dddt:post-loan-api
it-dev:dddt:quickpass-direct-pay
it-dev:dddt:repayment-dd
it-dev:dddt:unified-monitor-infras
it-dev:dddt:wappay-monitor
it-dev:bank-vendor:jetpay-alipay-single
it-dev:bank-vendor:jetpay-chinapay-single
it-dev:bank-vendor:jetpay-lianlian-single
it-dev:bank-vendor:jetpay-proxy-baofu-sa-single
it-dev:bank-vendor:jetpay-proxy-baofu-single
it-dev:bank-vendor:jetpay-proxy-boc-single
it-dev:bank-vendor:jetpay-proxy-jd-single
it-dev:bank-vendor:jetpay-proxy-yinyin-single
it-dev:bank-vendor:jetpay-vendor-ccb-single
it-dev:bank-vendor:jetpay-vendor-ebu-single
it-dev:bank-vendor:jetpay-vendor-icbc-sz-single
it-dev:bank-vendor:jetpay-vendor-package-psbcwh
it-dev:bank-vendor:jetpay-vendor-proxy-base
it-dev:bank-vendor:jetpay-vendor-proxy-batch-base
it-dev:bank-vendor:jetpay-vendor-proxy-batch-runtime
it-dev:bank-vendor:jetpay-vendor-proxy-batch-runtime-abc
it-dev:bank-vendor:jetpay-vendor-proxy-batch-runtime-baofu
it-dev:bank-vendor:jetpay-vendor-proxy-batch-runtime-boc
it-dev:bank-vendor:jetpay-vendor-proxy-batch-runtime-ccb
it-dev:bank-vendor:jetpay-vendor-proxy-batch-runtime-ebu
it-dev:bank-vendor:jetpay-vendor-proxy-batch-runtime-icbc-tj
it-dev:bank-vendor:jetpay-vendor-proxy-batch-runtime-jdpay
it-dev:bank-vendor:jetpay-vendor-proxy-batch-runtime-psbcwh
it-dev:bank-vendor:jetpay-vendor-proxy-package-abc
it-dev:bank-vendor:jetpay-vendor-proxy-package-baofu
it-dev:bank-vendor:jetpay-vendor-proxy-package-boc
it-dev:bank-vendor:jetpay-vendor-proxy-package-ccb
it-dev:bank-vendor:jetpay-vendor-proxy-package-ebu
it-dev:bank-vendor:jetpay-vendor-proxy-package-icbc-tj
it-dev:bank-vendor:jetpay-vendor-proxy-package-jdpay
it-dev:bank-vendor:jetpay-vendor-proxy-single-base
it-dev:bank-vendor:jetpay-vendor-proxy-transaction-wechat
it-dev:bank-vendor:jetpay-vendor-psbc-single
it-dev:bank-vendor:jetpay-vendor-single-starter
it-dev:bank-vendor:jetpay-wechat-single
it-dev:bank-vendor:mysql-db-backup
it-dev:ddap:ddap-online-abc
it-dev:ddap:ddap-online-auth-sync
it-dev:ddap:ddap-online-baofoo
it-dev:ddap:ddap-online-baofu-al
it-dev:ddap:ddap-online-baofu-callback
it-dev:ddap:ddap-online-boc
it-dev:ddap:ddap-online-boc-customer
it-dev:ddap:ddap-online-ccb
it-dev:ddap:ddap-online-core
it-dev:ddap:ddap-online-cp
it-dev:ddap:ddap-online-dao
it-dev:ddap:ddap-online-distributor
it-dev:ddap:ddap-online-ebu
it-dev:ddap:ddap-online-gateway
it-dev:ddap:ddap-online-icbc
it-dev:ddap:ddap-online-icbc-sz
it-dev:ddap:ddap-online-jd
it-dev:ddap:ddap-online-psbc
it-dev:ddap:ddap-online-yinyin
it-dev:ddap:ddme-auth-brain
it-dev:ddap:jd-dd-internal-auth
it-dev:ddap:jd-feedback-internal-auth
it-dev:ddap:jetpay-bank-auth-monitor
it-dev:ddap:nc-alipay-dd-auth-gateway
it-dev:ddap:no-alipaync-dd-auth-gateway
it-dev:ddap:no-dd-cancel-authorization-abc
it-dev:ddap:no-dd-cancel-authorization-baofu
it-dev:ddap:no-dd-cancel-authorization-boc
it-dev:ddap:no-dd-cancel-authorization-ccb
it-dev:ddap:no-dd-cancel-authorization-chinapay
it-dev:ddap:no-dd-cancel-authorization-core
it-dev:ddap:no-dd-cancel-authorization-ebu
it-dev:ddap:no-dd-cancel-authorization-icbcsz-new
it-dev:ddap:no-dd-cancel-authorization-icbctj
it-dev:ddap:no-dd-cancel-authorization-jdpay
it-dev:ddap:no-dd-cancel-authorization-yinyin
it-dev:ddap:no-ddap-online-auth-sync
it-dev:ddap:no-ddap-online-boc-customer
it-dev:ddap:no-ddap-online-core
it-dev:ddap:no-ddme-auth-brain
it-dev:ddap:no-wechat-dd-auth
it-dev:ddap:no-wechat-dd-auth-gateway
it-dev:ddap:wechat-dd-auth
it-dev:ddap:wechat-dd-auth-gateway
it-dev:instant-payment:bds
it-dev:instant-payment:bill
it-dev:instant-payment:commission
it-dev:instant-payment:commission-gw
it-dev:instant-payment:customerOoverpayment
it-dev:instant-payment:disbursement
it-dev:instant-payment:disbursement-gw
it-dev:instant-payment:disbursement-repay
it-dev:instant-payment:err-config
it-dev:instant-payment:hcp-bos
it-dev:instant-payment:hsw-autopay-cfc-rollout
it-dev:instant-payment:hsw-payment-history
it-dev:instant-payment:ka-new-commission
it-dev:instant-payment:pay-hub
it-dev:instant-payment:pay-parent
it-dev:instant-payment:payment-retailer-setting
it-dev:instant-payment:payments-data
it-dev:instant-payment:reconcile-bank
it-dev:instant-payment:retailer-report-info
it-dev:instant-payment:tipper-payment
it-dev:hs4repayment:abs-coupon-pay
it-dev:hs4repayment:abs-membership
it-dev:hs4repayment:abs-on-line-inquiry
it-dev:hs4repayment:al-dd-process-monitor-ws
it-dev:hs4repayment:asset-pledge-alarm
it-dev:hs4repayment:auth-notice
it-dev:hs4repayment:baofu-view
it-dev:hs4repayment:boss-bff
it-dev:hs4repayment:client-dd-auth-mgmt-ws
it-dev:hs4repayment:client-dd-authorization-statistics
it-dev:hs4repayment:dd-abc
it-dev:hs4repayment:dd-baofu
it-dev:hs4repayment:dd-cancel-authorization
it-dev:hs4repayment:dd-cancel-authorization-abc
it-dev:hs4repayment:dd-cancel-authorization-baofu
it-dev:hs4repayment:dd-cancel-authorization-boc
it-dev:hs4repayment:dd-cancel-authorization-ccb
it-dev:hs4repayment:dd-cancel-authorization-chinapay
it-dev:hs4repayment:dd-cancel-authorization-core
it-dev:hs4repayment:dd-cancel-authorization-distributor
it-dev:hs4repayment:dd-cancel-authorization-ebu
it-dev:hs4repayment:dd-cancel-authorization-icbcsz
it-dev:hs4repayment:dd-cancel-authorization-icbcsz-new
it-dev:hs4repayment:dd-cancel-authorization-icbctj
it-dev:hs4repayment:dd-cancel-authorization-jdpay
it-dev:hs4repayment:dd-cancel-authorization-yinyin
it-dev:hs4repayment:dd-response-status
it-dev:hs4repayment:dd-service-deactivate
it-dev:hs4repayment:ddme-reconciliation
it-dev:hs4repayment:direct-debit-response
it-dev:hs4repayment:hcc-huigou-monitor-ws
it-dev:hs4repayment:hsw-commission-query
it-dev:hs4repayment:hsw-common-nfs
it-dev:hs4repayment:hsw-incoming-pay-upload
it-dev:hs4repayment:hsw-payoff-email
it-dev:hs4repayment:hsw-repayment-channel
it-dev:hs4repayment:hsw-ssdd-noraml-ws
it-dev:hs4repayment:hsw-ssdd-path-ws
it-dev:hs4repayment:hsw-ssdd-result
it-dev:hs4repayment:hsw-ssdd-routing
it-dev:hs4repayment:hsw-ssdd-surprise
it-dev:hs4repayment:hsw-ssdd-transaction
it-dev:hs4repayment:jetpay-al-dd-search-result
it-dev:hs4repayment:jetpay-al-error-report
it-dev:hs4repayment:jetpay-al-process-monitoring
it-dev:hs4repayment:jetpay-al-single-channel
it-dev:hs4repayment:jetpay-boss-channel-rule
it-dev:hs4repayment:jetpay-boss-response-statistics
it-dev:hs4repayment:jetpay-boss-response-statistics-fast
it-dev:hs4repayment:jetpay-boss-surprise-result
it-dev:hs4repayment:jetpay-boss-transaction-overview
it-dev:hs4repayment:jetpay-ddservice-deactivate
it-dev:hs4repayment:jetpay-error-report
it-dev:hs4repayment:jetpay-error-report-fast
it-dev:hs4repayment:jetpay-package-monitor-ws
it-dev:hs4repayment:jetpay-router-api
it-dev:hs4repayment:jetpay-single-channel
it-dev:hs4repayment:jetpay-transaction-overview-fast
it-dev:hs4repayment:manual-instant-refund
it-dev:hs4repayment:no-non-dd-sync
it-dev:hs4repayment:no-payment-activity-monitor-ws
it-dev:hs4repayment:no-payment-order-monitor-ws
it-dev:hs4repayment:non-dd-monitor-ws
it-dev:hs4repayment:non-dd-sync
it-dev:hs4repayment:non-dd-sync-report
it-dev:hs4repayment:overpayment
it-dev:hs4repayment:paired-sms-notice
it-dev:hs4repayment:pay-notice
it-dev:hs4repayment:payment-activity-monitor-ws
it-dev:hs4repayment:payment-order-monitor-ws
it-dev:hs4repayment:psbc-bill-email
it-dev:hs4repayment:reconcile
it-dev:hs4repayment:reconcile-vendor2local
'''

def get_projects_scope():
    return list(filter(lambda x:x and len(x)>0, project_key_scope.split('\n')))


def check_sonar_report(namespace, projectname):
    url = f'http://sonarqube.prod.hccn/api/measures/component?component=it-dev:{namespace}:{projectname}&metricKeys=report&branch=master'
    res = requests.get(url, verify=False, auth=('jack.ji', 'In@202406'))
    res_json = json.loads(res.text)
    try:
        if res_json['component'] == None:
            return res.text
        if res_json['component']['measures'] == None or len(res_json['component']['measures']) == 0:
            return 'no sonar report'
        measures = res_json['component']['measures']
        for m in measures:
            if m['metric'] == 'report' and len(m['value']) > 10:
                return "sonar scan success"
        return 'no sonar report'
    except Exception as e:
        return e


if __name__ == '__main__':
    # git_url = get_git_url_from_sonar('dddt', 'al-alipay-repay-monitor')
    # print(get_issue_count_from_sonar('dddt', 'al-alipay-repay-monitor'))
    # l = get_projects('hs4repayment')
    l = get_projects_scope()
    write_sonar_scan_status_to_csv(l)
