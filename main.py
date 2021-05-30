from webflow_feeder_lib.football_api_methods import get_mathes_data
from pipelines import pipeline_main
import logging
import sys


logging.root.setLevel('DEBUG')
from pipelines import pipeline_main


# print(config)
# try to get the time line 
resp =  get_mathes_data('2021-03-06', '2021-03-31')

resp_json = resp.json()
if resp_json['errors']:
    logging.error("============== ERROR ==============")
    logging.error("Error str:{}".format(resp_json['errors']))
    sys.exit() 
raw_data_list =resp_json['response']
pipeline_main(raw_data_list)
