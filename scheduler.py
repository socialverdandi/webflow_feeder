from webflow_feeder_lib.football_api_methods import get_mathes_data_on_date
from pipelines import pipeline_main
import logging
import sys
import datetime


logging.root.setLevel('DEBUG')
from pipelines import pipeline_main

# get yesterday date
preDate = datetime.datetime.utcnow() - datetime.timedelta(days=1)
preDate_str = preDate.strftime('%Y-%m-%d')
logging.info('getting football match data on date:{}'.format(preDate_str))

resp =  get_mathes_data_on_date(preDate_str)

resp_json = resp.json()
if resp_json['errors']:
    logging.error("============== ERROR ==============")
    logging.error("Error str:{}".format(resp_json['errors']))
    sys.exit() 
raw_data_list =resp_json['response']
pipeline_main(raw_data_list)
