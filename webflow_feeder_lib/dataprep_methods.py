from dateutil import parser
import pytz
from thaiTeamName import teamName_dict
from config import config
thaiMonth_list = ['' , 'มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
def dataprep_mathcesOnDay(raw_data):
    # process single match data
    data = {}

    match_date = parser.parse(raw_data['fixture']['date']).astimezone(pytz.timezone("Asia/Bangkok"))
    date_str = match_date.strftime('%Y%m%d')

    # turn into weblflow time format
    data['date'] = match_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    data['fixture-id'] = raw_data['fixture']['id']
    # TODO: change into thai name
    data['home-team'] = raw_data['teams']['home']['name']
    data['home-logo'] = raw_data['teams']['home']['logo']
    data['home-score'] = raw_data['goals']['home']
    # data['home-article'] = 'None'
    data['away-team'] = raw_data['teams']['away']['name']
    data['away-logo'] = raw_data['teams']['away']['logo']
    data['away-score'] = raw_data['goals']['away']
    # data['away-article'] = 'None'
    # data['score-article'] = 'None'

    data['name'] = "Season{}_{}_{}_vs_{}".format(config['SEASON'], 
                                                date_str, 
                                                data['home-team'].replace(" ", "_"), 
                                                data['away-team'].replace(" ", "_"))

    data['home-team'] = teamName_dict.get(data['home-team']) or data['home-team']
    data['away-team'] = teamName_dict.get(data['away-team']) or data['away-team']
    data['_archived'] = False
    data['_draft'] = False
    # data['slug'] = "{}_{}_{}".format(date_str, 
    #                                     data['home_team'].replace(" ", "_"), 
    #                                     data['away_team'].replace(" ", "_"))
                                        
    helper_data = {
        'match_date': match_date
    }
    return  helper_data, data

def dataprep_matchesInDays(raw_data):
    data = {}
    # print('raw_data:{}'.format(raw_data))
    data['name'] = raw_data['date'].strftime('%Y%m%d')
    thaiYear = raw_data['date'].year + 543
    thaiMonth = thaiMonth_list[raw_data['date'].month]
    data['display-name'] = "{} {} {}".format(raw_data['date'].day, thaiMonth, thaiYear)
    data['date'] = int(raw_data['date'].strftime('%Y%m%d'))
    data['match-list'] = raw_data['data_list']
    data['_archived'] = False
    data['_draft'] = False
    
    helper_data = {'match_date':raw_data['date']}
    return helper_data, data
    # month_str = raw_data['date'].strftime('%Y%m')
    # return month_str, data

def dataprep_matchesInMonths(raw_data):
    data = {}
    data['name'] = raw_data['month_str']
    thaiYear = raw_data['date'].year + 543
    thaiMonth = thaiMonth_list[raw_data['date'].month]
    data['display-name'] = "ผลการแข่งขันพรีเมียร์ลีก {}/{} ประจำเดือน{} {}".format(config['SEASON'], 
                                                                        raw_data['date'].year, thaiMonth, thaiYear)
    data['year-month'] = int(raw_data['month_str'])
    data['day-list'] = raw_data['data_list']
    data['_archived'] = False
    data['_draft'] = False
    helper_data ={}
    return helper_data, data

dataprep  = {
    'MATCHES_ON_DAY':dataprep_mathcesOnDay,
    'MATCHES_IN_DAYS':dataprep_matchesInDays,
    'MATCHES_IN_MONTHS':dataprep_matchesInMonths,
}