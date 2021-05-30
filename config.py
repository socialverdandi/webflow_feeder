import os
import logging
import sys

    
key_list = [
    'FOOTBALL_API_URL',
    'FOOTBALL_API_TOKEN',
    'LEAGUE_ID',
    'WEBFLOW_API_URL',
    'WEBFLOW_API_VERSION',
    'WEBFLOW_API_TOKEN',
    'MATCHES_ON_DAY_ID',
    'MATCHES_IN_DAYS_ID',
    'MATCHES_IN_MONTHS_ID',
    'SEASON'

]
config = {}
for key in key_list:
    config[key] = os.environ.get(key) 
    logging.info("key:{} hace value:{}".format(key, config[key]))