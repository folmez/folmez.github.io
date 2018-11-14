import bulten_tools as bt

def test_whether_all_mac_details_are_str():
    for file in bt.get_bulten_filenames():
        match_list = bt.get_matches(file)
        for match in match_list:
            assert type(match.date) is str
            assert type(match.day) is str
            assert type(match.place) is str
            assert type(match.time) is str
            assert type(match.home) is str
            assert type(match.away) is str
            assert type(match.league) is str
            assert type(match.group) is str
            assert type(match.ref) is str
            assert type(match.ar1) is str
            assert type(match.ar2) is str
            assert type(match.fourth) is str
            assert type(match.observer) is str

def test_bulten_filenames():
    # Checks bultens start with an increasing identifying week number:
    # 01, 02, 03, ..., 10, 11, ...
    count = 1
    for file in bt.get_bulten_filenames():
        assert int(bt.get_bulten_week_number_as_str(file)) is count
        count = count+1

def test_split_date_and_day():
    assert bt.split_date_and_day('7 Eylul 1986, Pazar') == \
                                                    ('7 Eylul 1986', 'Pazar')

def test_times():
    for file in bt.get_bulten_filenames():
        match_list = bt.get_matches(file)
        for match in match_list:
            assert bt.is_time(match.time)

def test_dates():
    for file in bt.get_bulten_filenames():
        match_list = bt.get_matches(file)
        for match in match_list:
            assert match.date[-4::] in ['2018', '2019']

def test_leagues():
    for file in bt.get_bulten_filenames():
        match_list = bt.get_matches(file)
        for match in match_list:
            assert match.league in ['SAL', 'U12', 'U15B', 'U15A','U17A',\
                                    'U17B', '1AL', 'ELİT U15', 'ELİT U16',\
                                    'BGL U15', 'BGL U16', 'BGL U17',\
                                    'BGL U19','KDN', 'ELİT U14', 'ELİT U17',\
                                    'ELİT U19', 'ÖZEL']
