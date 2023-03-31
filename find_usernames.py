# list all the active users associated to a gitlab parent group
import requests
from requests.adapters import HTTPAdapter, Retry

URL = "https://gitlab.example.com/api/v4/projects/"
access_token = "Access-Token"
parent_group_id = "parent group ID"

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))

# list of all the projects obtained in find_all_projects.py
projects_non_archive = {"project_id": "project_name"}

email_set = set()

for old_projects in projects_non_archive:
    old_response = session.get(URL + str(old_projects) + "/members",
                               headers={"Authorization": "Bearer " + access_token}, timeout=None).json()
    for response in old_response:
        if response['state'] == "active":
            username = response['username']
            email_set.add(username)

old_response = session.get("https://gitlab.example.com/api/v4/groups/" + parent_group_id + "/members",
                           headers={"Authorization": "Bearer " + access_token}, timeout=None).json()
for response in old_response:
    if response['state'] == "active":
        username = response['username']
        email_set.add(username)

print(email_set)
