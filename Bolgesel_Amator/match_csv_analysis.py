from datetime import datetime
import TFF_match

def create_match_from_csv_row(row):
    return TFF_match.match(int(row[0]), \
                    datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'), \
                    row[2], int(row[3]), row[4], int(row[5]), row[6], \
                    int(row[7]), row[8], int(row[9]), row[10], \
                    int(row[11]), row[12], int(row[13]), row[14], \
                    int(row[15]), row[16], int(row[17]), int(row[18]))

def get_match_id_from_csv_row(row):
    return int(row[0])

def get_datetime_from_csv_row(row):
    return datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')

def get_organizasyon_name_from_csv_row(row):
    return row[2]

def get_hakem_id_from_csv_row(row):
    return int(row[3])

def get_hakem_name_from_csv_row(row):
    return row[4]

def get_ar1_id_from_csv_row(row):
    return int(row[5])

def get_ar1_name_from_csv_row(row):
    return row[6]

def get_ar2_id_from_csv_row(row):
    return int(row[7])

def get_ar2_name_from_csv_row(row):
    return row[8]

def get_dort_id_from_csv_row(row):
    return int(row[9])

def get_dort_name_from_csv_row(row):
    return row[10]

def get_stad_id_from_csv_row(row):
    return int(row[11])

def get_stad_name_from_csv_row(row):
    return row[12]

def get_home_team_id_from_csv_row(row):
    return int(row[13])

def get_home_team_name_from_csv_row(row):
    return row[14]

def get_away_team_id_from_csv_row(row):
    return int(row[15])

def get_away_team_name_from_csv_row(row):
    return row[16]

def get_home_team_skor_from_csv_row(row):
    return int(row[17])

def get_away_team_skor_from_csv_row(row):
    return int(row[18])
