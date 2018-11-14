import pandas as pd
import os
import sys
import math

class match:
    def __init__(self, date, day, place, time, home, away, league, group,\
                                        ref, ar1, ar2, fourth, observer):
        self.date = date
        self.day = day
        self.place = place
        self.time = time
        self.home = home
        self.away = away
        self.league = league
        self.group = group
        self.ref = ref
        self.ar1 = return_empty_str_if_nan(ar1)
        self.ar2 = return_empty_str_if_nan(ar2)
        self.fourth = return_empty_str_if_nan(fourth)
        self.observer = return_empty_str_if_nan(observer)

    def print_match_details(self):
        print(self.home, "vs", self.away)

    def is_this_a_league_game(self):
        # Home and away teams are split. When the match is a tournament game
        # the away team is input as empty string
        return self.away is not ''

def get_matches(bulten_filename):
    df = parse_bulten(bulten_filename)
    match_list = []
    for index, row in df.iterrows():
        # If the row starts with date and day, rest of the column is nan
        # TODO: Check that first row of each bulten is date/day and second row
        #       is the place
        if is_date_and_day(row['Saat']):
            current_date, current_day = split_date_and_day(row['Saat'])
        else:
            if not is_time(row['Saat']):
                current_place = row['Saat']
            else:
                # This is a match. Record it
                current_time = row['Saat']
                current_home, current_away = \
                                        split_home_and_away(row['Takımlar'])
                current_league, current_group = \
                                        split_league_and_group(row['Kategori'])
                match_list.append(match(current_date, current_day, current_place,\
                    current_time, current_home, current_away, \
                    current_league, current_group ,\
                    row['Hakem'], row['1. Yrd. Hakem'], row['2. Yrd. Hakem'],\
                    row['4. Hakem'], row['Gözlemci']))
    return match_list

def get_all_matches():
    bulten_filenames = get_bulten_filenames()
    match_list = get_matches(bulten_filenames[0])
    for file in bulten_filenames[1::]:
        match_list = match_list + get_matches(file)
    return match_list

def get_last_weeks_matches():
    bulten_filenames = get_bulten_filenames()
    return get_matches(bulten_filenames[-1])

def get_bulten_html_foldername():
    BULTEN_HTML_FOLDERNAME = "1819_bultenler_htmls"
    return BULTEN_HTML_FOLDERNAME

def get_bulten_foldername():
    BULTEN_FOLDERNAME = "1819_bultenler"
    return BULTEN_FOLDERNAME

def get_bulten_filenames():
    bulten_foldername = get_bulten_foldername()
    bulten_filenames = [os.path.join(bulten_foldername, file) \
                            for file in sorted(os.listdir(bulten_foldername)) \
                            if file.endswith(".xlsx")]
    return bulten_filenames

def print_all_bulten_filenames():
    bulten_filenames = get_bulten_filenames()
    for file in bulten_filenames:
        print(file)

def parse_bulten(bulten_filename):
    bulten_xl = pd.ExcelFile(bulten_filename)
    bulten_sheet_names = bulten_xl.sheet_names
    df = bulten_xl.parse(bulten_sheet_names[0])
    return df

def create_bulten_database(bulten_filename):
    pass

def is_date_and_day(str):
    return ", " in str

def is_time(str):
    return ":" in str and len(str) is 5

def split_date_and_day(date_and_day_str):
    if is_date_and_day(date_and_day_str):
        date_str, day_str = date_and_day_str.split(", ")
        return date_str, day_str
    else:
        raise Exception(f"({date_and_day_str}) must be: 07 Eylul 1986. Pazar")
        sys.exit(1)

def split_home_and_away(home_and_away_str):
    if " - " in home_and_away_str:
        home_str, away_str = home_and_away_str.split(" - ")
    else:
        home_str, away_str = [home_and_away_str, '']
    return home_str, away_str

def list_unique_leagues():
    unique_leagues = []
    for match in get_all_matches():
        if match.league not in unique_leagues:
            unique_leagues.append(match.league)
    return unique_leagues

def split_league_and_group(match_cat_str):
    # Amator
    orig_list = ['S.A.L. - ', 'U-12 - ', 'U15 B - ', 'U-15 A - ', \
                        'U-17 A - ', 'U17 B - ', '1.AL. - ']
    cat_list = ['SAL', 'U12', 'U15B', 'U15A',\
                        'U17A', 'U17B', '1AL']
    for i in range(len(orig_list)):
        orig_name = orig_list[i]
        simple_name = cat_list[i]
        if match_cat_str[0:len(orig_name)] == orig_name and \
                                            match_cat_str[-5::] == '.GRUP':
            return simple_name, \
                    get_group_number_as_str(match_cat_str, orig_name, '.GRUP')

    # Elite and BGL
    if match_cat_str[0:6] == 'ELİT U' and \
                        (match_cat_str[0:8] == match_cat_str[-8::]):
        return 'ELİT ' + match_cat_str[5:8], '0' # '0': no group number
    elif match_cat_str[0:5] == 'BGL U' and \
                        (match_cat_str[0:7] == match_cat_str[-7::]):
        return 'BGL ' + match_cat_str[4:7], '0' # '0': no group number

    # Exceptions
    if match_cat_str == 'U16 - ELİT U16':
        return 'ELİT U16', '0' # '0': no group number
    elif match_cat_str == 'U15 - ELİT U15':
        return 'ELİT U15', '0' # '0': no group number
    elif match_cat_str == 'Kdn. - KADINLAR LİGİ':
        return 'KDN', '0' # '0': no group number

    return match_cat_str, ''

def get_group_number_as_str(match_cat_str, str1, str2):
    j = match_cat_str.find(str2)
    return match_cat_str[len(str1):j]

def return_empty_str_if_nan(nan_or_str):
    if type(nan_or_str) is str:
        return nan_or_str
    elif math.isnan(nan_or_str):
        return ''

def get_bulten_week_number_as_str(bulten_filename):
    x = len(get_bulten_foldername())
    return bulten_filename[x+1:x+3]

def is_this_an_efso_mac(ref_name, mac):
    return ref_name in [mac.ref, mac.ar1, mac.ar2]

def get_efso_list():
    return ['MÜCAHİD ADEM ÇELEBİ']
