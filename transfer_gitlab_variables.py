""" This code is used to transfer CI/CD variables from one gitlab repo to another after running the missing_variables.py
and getting the list of mapping"""

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


missing_project_list = [{'Old_project_id': '9932', 'New_project_id': '44108368', 'No_of_missing_vars': 0},
                        {'Old_project_id': '9863', 'New_project_id': '44108374', 'No_of_missing_vars': 0},
                        {'Old_project_id': '9107', 'New_project_id': '44108435', 'No_of_missing_vars': 0},
                        {'Old_project_id': '9046', 'New_project_id': '44108480', 'No_of_missing_vars': 0},
                        {'Old_project_id': '8067', 'New_project_id': '44108492', 'No_of_missing_vars': 0},
                        {'Old_project_id': '7867', 'New_project_id': '44108499', 'No_of_missing_vars': 0},
                        {'Old_project_id': '7657', 'New_project_id': '44108508', 'No_of_missing_vars': 0},
                        {'Old_project_id': '7624', 'New_project_id': '44108514', 'No_of_missing_vars': 0},
                        {'Old_project_id': '7025', 'New_project_id': '44108521', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6962', 'New_project_id': '44108538', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6661', 'New_project_id': '44108557', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6504', 'New_project_id': '44108598', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6475', 'New_project_id': '44108606', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6302', 'New_project_id': '44108608', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6225', 'New_project_id': '44108610', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6190', 'New_project_id': '44108612', 'No_of_missing_vars': 30},
                        {'Old_project_id': '15198', 'New_project_id': '44107582', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14616', 'New_project_id': '44107585', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14468', 'New_project_id': '44107588', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14304', 'New_project_id': '44107600', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14032', 'New_project_id': '44107626', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13941', 'New_project_id': '44107632', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13251', 'New_project_id': '44107678', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12868', 'New_project_id': '44107679', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12728', 'New_project_id': '44107716', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12706', 'New_project_id': '44107714', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12704', 'New_project_id': '44107720', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12685', 'New_project_id': '44107719', 'No_of_missing_vars': 36},
                        {'Old_project_id': '12548', 'New_project_id': '44107753', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12468', 'New_project_id': '44107771', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12129', 'New_project_id': '44107781', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12128', 'New_project_id': '44107788', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12096', 'New_project_id': '44107795', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11895', 'New_project_id': '44107800', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11851', 'New_project_id': '44107801', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11810', 'New_project_id': '44107808', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11803', 'New_project_id': '44107818', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11761', 'New_project_id': '44107838', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11537', 'New_project_id': '44107843', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11442', 'New_project_id': '44107852', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11372', 'New_project_id': '44107867', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11330', 'New_project_id': '44107871', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11320', 'New_project_id': '44107877', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11119', 'New_project_id': '44107883', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11078', 'New_project_id': '44107892', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11014', 'New_project_id': '44107899', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11013', 'New_project_id': '44107902', 'No_of_missing_vars': 0},
                        {'Old_project_id': '10721', 'New_project_id': '44107912', 'No_of_missing_vars': 0},
                        {'Old_project_id': '10200', 'New_project_id': '44107946', 'No_of_missing_vars': 0},
                        {'Old_project_id': '10199', 'New_project_id': '44107945', 'No_of_missing_vars': 0},
                        {'Old_project_id': '10185', 'New_project_id': '44108042', 'No_of_missing_vars': 0},
                        {'Old_project_id': '10135', 'New_project_id': '44108129', 'No_of_missing_vars': 0},
                        {'Old_project_id': '10134', 'New_project_id': '44108136', 'No_of_missing_vars': 0},
                        {'Old_project_id': '10133', 'New_project_id': '44108135', 'No_of_missing_vars': 0},
                        {'Old_project_id': '10093', 'New_project_id': '44108139', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6223', 'New_project_id': '44108787', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11370', 'New_project_id': '44109847', 'No_of_missing_vars': 0},
                        {'Old_project_id': '7055', 'New_project_id': '44109853', 'No_of_missing_vars': 0},
                        {'Old_project_id': '16168', 'New_project_id': '44108637', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15398', 'New_project_id': '44108638', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13466', 'New_project_id': '44108651', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13273', 'New_project_id': '44108659', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12985', 'New_project_id': '44108665', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12901', 'New_project_id': '44108675', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15687', 'New_project_id': '44108772', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15869', 'New_project_id': '44108795', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11227', 'New_project_id': '44108799', 'No_of_missing_vars': 0},
                        {'Old_project_id': '7095', 'New_project_id': '44108802', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6933', 'New_project_id': '44108804', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6734', 'New_project_id': '44108815', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6507', 'New_project_id': '44108820', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6191', 'New_project_id': '44108819', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13003', 'New_project_id': '44108826', 'No_of_missing_vars': 17},
                        {'Old_project_id': '12574', 'New_project_id': '44108836', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12214', 'New_project_id': '44108843', 'No_of_missing_vars': 19},
                        {'Old_project_id': '12213', 'New_project_id': '44108851', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11180', 'New_project_id': '44108948', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11179', 'New_project_id': '44108960', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11177', 'New_project_id': '44108971', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11176', 'New_project_id': '44108986', 'No_of_missing_vars': 0},
                        {'Old_project_id': '16051', 'New_project_id': '44108867', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15695', 'New_project_id': '44108879', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15581', 'New_project_id': '44108880', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15248', 'New_project_id': '44108890', 'No_of_missing_vars': 4},
                        {'Old_project_id': '15194', 'New_project_id': '44108908', 'No_of_missing_vars': 4},
                        {'Old_project_id': '14588', 'New_project_id': '44109083', 'No_of_missing_vars': 14},
                        {'Old_project_id': '14179', 'New_project_id': '44109104', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12974', 'New_project_id': '44109153', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12946', 'New_project_id': '44109157', 'No_of_missing_vars': 16},
                        {'Old_project_id': '12819', 'New_project_id': '44109165', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12730', 'New_project_id': '44109183', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12576', 'New_project_id': '44109192', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12045', 'New_project_id': '44109882', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11977', 'New_project_id': '44109885', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14475', 'New_project_id': '44110371', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14442', 'New_project_id': '44110372', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14816', 'New_project_id': '44109902', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14798', 'New_project_id': '44109906', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14624', 'New_project_id': '44109904', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14587', 'New_project_id': '44109923', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14583', 'New_project_id': '44109937', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14562', 'New_project_id': '44109943', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14554', 'New_project_id': '44109977', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14521', 'New_project_id': '44109982', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14503', 'New_project_id': '44110010', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12322', 'New_project_id': '44110011', 'No_of_missing_vars': 2},
                        {'Old_project_id': '13344', 'New_project_id': '44110068', 'No_of_missing_vars': 1},
                        {'Old_project_id': '13248', 'New_project_id': '44110069', 'No_of_missing_vars': 1},
                        {'Old_project_id': '12531', 'New_project_id': '44110098', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15999', 'New_project_id': '44110121', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15005', 'New_project_id': '44110147', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14567', 'New_project_id': '44110144', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14563', 'New_project_id': '44110165', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14560', 'New_project_id': '44110171', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14558', 'New_project_id': '44110170', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14486', 'New_project_id': '44110205', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13420', 'New_project_id': '44110232', 'No_of_missing_vars': 0},
                        {'Old_project_id': '16139', 'New_project_id': '44109210', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11055', 'New_project_id': '44109229', 'No_of_missing_vars': 0},
                        {'Old_project_id': '6755', 'New_project_id': '44109317', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14476', 'New_project_id': '44110269', 'No_of_missing_vars': 9},
                        {'Old_project_id': '13572', 'New_project_id': '44110298', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13555', 'New_project_id': '44110306', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13371', 'New_project_id': '44110310', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13184', 'New_project_id': '44110317', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13179', 'New_project_id': '44110325', 'No_of_missing_vars': 2},
                        {'Old_project_id': '12818', 'New_project_id': '44110330', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14340', 'New_project_id': '44109332', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13442', 'New_project_id': '44109342', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15344', 'New_project_id': '44109383', 'No_of_missing_vars': 0},
                        {'Old_project_id': '13990', 'New_project_id': '44109399', 'No_of_missing_vars': 0},
                        {'Old_project_id': '11901', 'New_project_id': '44109413', 'No_of_missing_vars': 0},
                        {'Old_project_id': '9029', 'New_project_id': '44109687', 'No_of_missing_vars': 0},
                        {'Old_project_id': '9028', 'New_project_id': '44109717', 'No_of_missing_vars': 0},
                        {'Old_project_id': '9027', 'New_project_id': '44109703', 'No_of_missing_vars': 0},
                        {'Old_project_id': '9026', 'New_project_id': '44109701', 'No_of_missing_vars': 0},
                        {'Old_project_id': '9025', 'New_project_id': '44109708', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15873', 'New_project_id': '44109807', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14914', 'New_project_id': '44109821', 'No_of_missing_vars': 0},
                        {'Old_project_id': '14603', 'New_project_id': '44109826', 'No_of_missing_vars': 42},
                        {'Old_project_id': '13547', 'New_project_id': '44109824', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12987', 'New_project_id': '44109735', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12937', 'New_project_id': '44109741', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12869', 'New_project_id': '44110342', 'No_of_missing_vars': 0},
                        {'Old_project_id': '12247', 'New_project_id': '44109830', 'No_of_missing_vars': 0},
                        {'Old_project_id': '10728', 'New_project_id': '44109841', 'No_of_missing_vars': 0},
                        {'Old_project_id': '15570', 'New_project_id': '44109763', 'No_of_missing_vars': 14},
                        {'Old_project_id': '14291', 'New_project_id': '44109785', 'No_of_missing_vars': 6}]

for old_project in missing_project_list:
    if old_project['No_of_missing_vars'] > 0:
        print("migrating variables for ", old_project['Old_project_id'])
        transfer_vars(str(old_project['Old_project_id']), str(old_project['New_project_id']))
