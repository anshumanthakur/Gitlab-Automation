""" This code is used for gitlab migration,
when you need to validate your gitlab project mapping from project_mapping.py"""

import requests
from requests.adapters import HTTPAdapter, Retry

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))

old_URL = "https://gitlab.example.com/api/v4/projects/"
new_url = "https://gitlab.com/api/v4/projects/"

old_access_token = "Access token from old repo"
new_access_token = "Access token from new repo"

project_mapping = {"old_project_id": "new project ID"}

projects_found = []
projects_not_found = []


def temp():
    for old_project in project_mapping:
        search_response_old = session.get(old_URL + str(old_project),
                                          headers={"Authorization": "Bearer " + old_access_token},
                                          timeout=None).json()
        search_response_new = session.get(new_url + str(project_mapping[old_project]),
                                          headers={"Authorization": "Bearer " + new_access_token},
                                          timeout=None).json()
        print(search_response_old['name'], ":", search_response_new['name'])
        if search_response_new['path_with_namespace'].lower().find(
                search_response_old['path_with_namespace'].lower()) == -1:
            print(search_response_old['name'], ":", search_response_new['name'], "project not found")
            print(str(old_project), ":", str(project_mapping[old_project]))
            projects_not_found.append(old_project)


temp()

print(projects_found)
print(projects_not_found)
old_URL = old_URL + "10009"
search_response = requests.get(old_URL,
                               headers={"Authorization": "Bearer " + old_access_token},
                               timeout=None).json()
print(len(search_response))
print(search_response)
