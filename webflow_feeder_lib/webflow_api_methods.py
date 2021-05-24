import requests
from config import config
import sys
import logging


headers = {
    'accept-version': config['WEBFLOW_API_VERSION'],
    "Authorization" : "Bearer {}".format(config['WEBFLOW_API_TOKEN'])
}

def get_current_collection_data(collection_id_str):
    collection_id = config[collection_id_str]
    resp = requests.get("{}/collections/{}/items".format(config['WEBFLOW_API_URL'], collection_id),
                    headers=headers)     
    resp_data = resp.json()
    if resp.status_code != 200:
        logging.error("====================== ERROR ======================")
        logging.error("cannot get data from collection_id:{}  with following error:{}".format(collection_id,resp_data))
        sys.exit()
    return resp_data['items']


def create_collection_item(collection_id_str, data):
    collection_id = config[collection_id_str]
    body_data = {
        'fields':data,
        'collection_id':collection_id 
    }
    resp = requests.post("{}/collections/{}/items".format(config['WEBFLOW_API_URL'], collection_id),
                    headers=headers,
                    json=body_data)     
    resp_data = resp.json()
    if resp.status_code != 200:
        logging.error("====================== ERROR ======================")
        logging.error("cannot post new item with following error:{}".format(resp_data))
        sys.exit()
    return True, resp_data



def update_collection_item(collection_id_str, matched_data, data):
    collection_id = config[collection_id_str]
    item_id = matched_data['_id']
    matched_data.pop('_id')
    matched_data.pop('updated-on')
    matched_data.pop('updated-by')
    matched_data.pop('created-on')
    matched_data.pop('created-by')
    
    if collection_id_str == 'MATCHES_IN_DAYS_ID':
        update_col = 'match-list'
    else:
        update_col ='day-list'

    matched_data[update_col].append(data[update_col])

    body_data = {
        'fields':matched_data,
        'collection_id':collection_id,
        'item_id':item_id
    }
    resp = requests.put("{}/collections/{}/items/{}".format(config['WEBFLOW_API_URL'], collection_id, item_id),
                    headers=headers,
                    json=body_data)     
    resp_data = resp.json()
    if resp.status_code != 200:
        logging.error("====================== ERROR ======================")
        logging.error("cannot post new item with following error:{}".format(resp_data))
        sys.exit()
    return True, resp_data

check_col ={
    'MATCHES_ON_DAY_ID':'fixture-id',
    'MATCHES_IN_DAYS_ID':'date',
    'MATCHES_IN_MONTHS_ID':'year-month'
}

def check_item_exists(collection_id_str,  data, current_data_list):
    col_name = check_col[collection_id_str]
    is_match = False
    matched_data = None
    # print("data:{}, current_data_list:{}".format(data, current_data_list))
    for current_data in current_data_list:
        if current_data[col_name] == data[col_name]:
            is_match = True
            matched_data = current_data
            return is_match, matched_data

    return is_match, matched_data

def post_collection_item(collection_id_str, data, current_data_list):
    is_match, matched_data = check_item_exists(collection_id_str,  data, current_data_list)
    if (collection_id_str=='MATCHES_ON_DAY_ID') and is_match:
        logging.warn("the match with fixture-id:{} already exist. the script will skip".format(data['fixture-id']))
        return False, {}

    if is_match:
        logging.info("collection already exists. Updating the data..")
        return update_collection_item(collection_id_str, matched_data, data)
        
    logging.info("collection is not exists. creating the collection..")
    return create_collection_item(collection_id_str, data)