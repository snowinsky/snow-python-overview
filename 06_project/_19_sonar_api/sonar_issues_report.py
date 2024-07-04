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
        return list(filter(lambda x:x['type'] == 'scm', res_json['links']))[0]['url']
    except Exception as e:
        print("get_git_url_from_sonar", name_space, project_name, e)
        return ''


def get_issue_count_from_sonar(name_space, project_name):
    metricKeys = ','.join("violations,blocker_violations,critical_violations,major_violations,info_violations,minor_violations".split(','))
    url = f"http://sonarqube.prod.hccn/api/measures/component?component=it-dev:{name_space}:{project_name}&metricKeys={metricKeys}"
    headers = {
        'Authorization': 'Basic amFjay5qaTpJbkAyMDI0MDY='
    }
    response = requests.request("GET", url, headers=headers)
    res_text_json = response.text
    res_json = json.loads(res_text_json)
    try:
        l = res_json['component']['measures']
        if l == None or len(l) == 0:
            return [
                {'metric': 'major_violations', 'value': '-1', 'bestValue': False
                },
                {'metric': 'minor_violations', 'value': '-1', 'bestValue': False
                },
                {'metric': 'critical_violations', 'value': '-1', 'bestValue': False
                },
                {'metric': 'blocker_violations', 'value': '-1', 'bestValue': False
                },
                {'metric': 'info_violations', 'value': '-1', 'bestValue': True
                },
                {'metric': 'violations', 'value': '-1', 'bestValue': False
                }
            ]
        else:
            return l
    except Exception as e:
        print("get_issue_count_from_sonar", name_space, project_name, e)
        return [
            {'metric': 'major_violations', 'value': '-1', 'bestValue': False
            },
            {'metric': 'minor_violations', 'value': '-1', 'bestValue': False
            },
            {'metric': 'critical_violations', 'value': '-1', 'bestValue': False
            },
            {'metric': 'blocker_violations', 'value': '-1', 'bestValue': False
            },
            {'metric': 'info_violations', 'value': '-1', 'bestValue': True
            },
            {'metric': 'violations', 'value': '-1', 'bestValue': False
            }
        ]

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
    while(True):
        l = get_projects_by_page(name_space, page)
        if len(l) == 0:
            return project_key_list
        else:
            project_key_list = project_key_list + l
            page = page + 1


name_space_list = ('dddt', 'bank-vendor', 'ddap', 'instant-payment', 'hs4repayment')

if __name__ == '__main__':
    # git_url = get_git_url_from_sonar('dddt', 'al-alipay-repay-monitor')
    # print(get_issue_count_from_sonar('dddt', 'al-alipay-repay-monitor'))
    # l = get_projects('hs4repayment')

    with open("D://doc/payment_project_sonar_reports_summary_v01.txt", 'w') as f:
        f.write(','.join(["project_name", 'git_url', 'blocker', 'critical', 'major', 'minor', 'info', 'report_url', 'author']))
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

