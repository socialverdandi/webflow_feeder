# data pipeline to process the date from football api and make it ready to be populated in webflow website

import requests
import logging
from webflow_feeder_libdataprep_methods import dataprep
from webflow_feeder_libdatapost_methods import datapost
from webflow_feeder_libwebflow_api_methods import *
import sys
from config import config
from tqdm import tqdm




def pipeline_collection(collection_type, raw_data_list):
    logging.info("populate data in collection:{}".format(collection_type))
    collection_id_str = collection_type + '_ID'
    #init result_data
    result_data = {}
    current_data_list = get_current_collection_data(collection_id_str)

    for raw_data in tqdm(raw_data_list):
        if collection_type != 'MATCHES_ON_DAY':
            # MATCHES_ON_DAY is a list but other collection are dict
            raw_data = raw_data_list[raw_data]

        helper_data, data = dataprep[collection_type](raw_data)
        
        collection_id = config[collection_id_str]
        isSuccess, resp_data = post_collection_item(collection_id_str, data, current_data_list)
        if not isSuccess:
            # if not success just skip it
            continue
        result_data = datapost[collection_type](helper_data, resp_data, result_data)   
    return result_data

def pipeline_main(raw_data_list):
    result_data_1 = pipeline_collection('MATCHES_ON_DAY', raw_data_list)
    result_data_2 = pipeline_collection('MATCHES_IN_DAYS', result_data_1)
    pipeline_collection('MATCHES_IN_MONTHS', result_data_2)
    logging.info(" +++++++++ pipeline complete +++++++++")
