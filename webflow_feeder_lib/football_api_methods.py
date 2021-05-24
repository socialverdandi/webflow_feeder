import requests
from config import config
import logging
import sys

headers = {
    'x-apisports-key': config['FOOTBALL_API_TOKEN']
}

def get_mathes_data(from_date, to_data):

    payload = {'league': config['LEAGUE_ID'] ,'season':config['SEASON'], 'from': from_date, 'to':to_data}

    return  requests.get(config['FOOTBALL_API_URL'] + '/fixtures', headers=headers, params=payload)

def get_team_name():
    payload = {'league': config['LEAGUE_ID'] ,'season':config['SEASON']}

    resp = requests.get(config['FOOTBALL_API_URL'] + '/teams', headers=headers, params=payload)
    resp_json = resp.json()
    if resp_json['errors']:
        logging.error("============== ERROR ==============")
        logging.error("Error str:{}".format(resp_json['errors']))
        sys.exit() 
    team_name_list = []
    raw_team_list = resp_json['response']
    for raw_team in raw_team_list:
        team_name_list.append(raw_team['team']['name'])
    return team_name_list