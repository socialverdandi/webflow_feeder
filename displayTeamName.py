from webflow_feeder_libfootball_api_methods import get_team_name
from pipelines import pipeline_main
import logging
import sys


logging.root.setLevel('INFO')
from pipelines import pipeline_main


# print(config)
# try to get the time line 
resp =  get_team_name()

print(resp)


