""" This code is used to find out missing variables from one gitlab repository to
another and create a list of dictionary containing old project and new project and the no. of missing variables"""

import requests
from requests.adapters import HTTPAdapter, Retry

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))


def transfer_vars(old_project_id, new_project_id):
    old_project_id = old_project_id
    new_project_id = new_project_id
    old_URL = "https://gitlab.example.com/api/v4/projects/"
    new_url = "https://gitlab.com/api/v4/projects/"
    old_URL = old_URL + old_project_id + "/variables?&per_page=100"
    new_url = new_url + new_project_id + "/variables?&per_page=100"
    old_access_token = "Access token from old repo"
    new_access_token = "Access token from new repo"

    missing_item_count = 0
    old_response = session.get(old_URL, headers={"Authorization": "Bearer " + old_access_token}, timeout=None).json()
    print(old_response)
    new_response = session.get(new_url, headers={"Authorization": "Bearer " + new_access_token}, timeout=None).json()

    for response in new_response:
        try:
            response.pop('raw')
        except Exception as e:
            print(e)
            raise e
    print(new_response)
    missing_items = []
    try:
        if len(old_response) > 0:
            for var in old_response:
                if var not in new_response:
                    missing_items.append(var)
            print("count of missing item", len(missing_items))
        else:
            print("no variables to compare")
    except Exception as e:
        print(e)
        raise e

    def migrate_vars():
        for missing_item in missing_items:
            form_data = {}
            for keys in missing_item:
                form_data[keys] = missing_item[keys]
            print(form_data)
            create_var_response = session.post(new_url, data=form_data,
                                               headers={"Authorization": "Bearer " + new_access_token},
                                               timeout=None).json()
            print("above variable has been migrated")

    migrate_vars()


missing_project_list = [{'Old_project_id': 'project_id', 'New_project_id': 'project_id', 'No_of_missing_vars': 6}]

for old_project in missing_project_list:
    if old_project['No_of_missing_vars'] > 0:
        print("migrating variables for ", old_project['Old_project_id'])
        transfer_vars(str(old_project['Old_project_id']), str(old_project['New_project_id']))
