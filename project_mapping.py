""" This code is used for gitlab migration,
when you need to map your repos from the old repo to the projects in the new repo"""

import requests
from requests.adapters import HTTPAdapter, Retry

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))


def get_project_mapping(project_list):
    old_URL = "https://gitlab.example.com/api/v4/projects/"  # old gitlab link
    new_url = "https://gitlab.com/api/v4/projects?search="  # new gitlab link
    old_access_token = "Access token from old repo"
    new_access_token = "Access token from new repo"

    projects_found = []
    projects_not_found = {}
    project_mapping = {}

    def temp():
        for old_projects in project_list:
            print("searching for", old_projects)
            value = project_list[old_projects].lower()

            search_response_old = session.get(old_URL + str(old_projects),
                                              headers={"Authorization": "Bearer " + old_access_token},
                                              timeout=None).json()

            string_to_search = search_response_old['path_with_namespace'].lower()

            search_response_new = session.get(new_url + str(value),
                                              headers={"Authorization": "Bearer " + new_access_token},
                                              timeout=None).json()

            if len(search_response_new) > 0:
                project_found_flag = False
                for response in search_response_new:
                    if response['path_with_namespace'].find(string_to_search) != -1 and str(value) == response[
                        'path'].lower():
                        projects_found.append(old_projects)
                        project_mapping[old_projects] = response['id']
                        print("project found")
                        project_found_flag = True
                        break
                if not project_found_flag:
                    print("project not found but length > 0")
                    projects_not_found[old_projects] = str(value)
            else:
                projects_not_found[old_projects] = str(value)
                print("project not found")

    temp()

    print(projects_found)
    print(projects_not_found)
    print(project_mapping)


# list of all the projects obtained in find_all_projects.py
old_projects_non_archive = {"project_id": "project_name"}
print("running script for non archive")
get_project_mapping(old_projects_non_archive)

print(len(old_projects_non_archive))
