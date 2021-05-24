#data post processing to be ready to be process agaib in next pipeline
def datapost_mathcesOnDay(helper_data, data, result_data):
    date_str = helper_data['match_date'].strftime('%Y%m%d')
    if date_str in result_data:
        result_data[date_str]['data_list'].append(data['_id'])
    else:
        result_data[date_str] = {
                'date':helper_data['match_date'],
                'data_list':[data['_id']]
            }
    return result_data

def datapost_mathcesInDays(helper_data, data, result_data):
    month_str = helper_data['match_date'].strftime('%Y%m')
    if month_str in result_data:
        result_data[month_str]['data_list'].append(data['_id'])
    else:
        result_data[month_str] = {
                'month_str':month_str,
                'date':helper_data['match_date'],
                'data_list':[data['_id']]
            }
    return result_data

def datapost_matchesInMonthss(helper_data, data, result_data):
    # no post data since no higeher collection
    return {}, {}


datapost  = {
    'MATCHES_ON_DAY':datapost_mathcesOnDay,
    'MATCHES_IN_DAYS':datapost_mathcesInDays,
    'MATCHES_IN_MONTHS':datapost_matchesInMonthss,
}