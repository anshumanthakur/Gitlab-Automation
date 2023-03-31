# code to find the list of all the repositories in all the groups under one gitlab parent

import requests

from requests.adapters import HTTPAdapter, Retry

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))

access_token = "Access-Token"
parent_group_id = "parent group ID"

projects_non_archive = {}
projects_archive = {}
group_ids = {}

project_url = "https://gitlab.example.com/api/v4/groups/" + parent_group_id + "/projects?&per_page=200&page=2"
projects_response = session.get(project_url,
                                headers={"Authorization": "Bearer " + access_token},
                                timeout=None).json()
for project in projects_response:
    try:
        if project['archived']:
            projects_archive[project['id']] = project['path']
        else:
            projects_non_archive[project['id']] = project['path']
    except:
        pass


def find_all_projects(group_id):
    project_url = "https://gitlab.example.com/api/v4/groups/" + group_id + "/projects?&per_page=200"
    projects_response = session.get(project_url,
                                    headers={"Authorization": "Bearer " + access_token},
                                    timeout=None).json()
    for project in projects_response:
        try:
            if project['archived']:
                projects_archive[project['id']] = project['path']
            else:
                projects_non_archive[project['id']] = project['path']
        except Exception as e:
            print(e)
            raise e


def find_all_subgroups(group_id):
    group_url = "https://gitlab.example.com/api/v4/groups/" + group_id + "/subgroups"
    group_details = session.get(group_url,
                                headers={"Authorization": "Bearer " + access_token},
                                timeout=None).json()

    if len(group_details) == 0:
        return
    for group in group_details:
        group_ids[group['id']] = group['path']
        find_all_subgroups(str(group['id']))


find_all_subgroups(parent_group_id)
find_all_projects(parent_group_id)
for group_id in group_ids:
    find_all_projects(str(group_id))

print(group_ids)
print("archive", projects_archive)
print("non archive", projects_non_archive)
