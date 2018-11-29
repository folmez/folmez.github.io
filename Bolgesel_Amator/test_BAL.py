import datetime
import csv
import TFF_match
import match_csv_analysis as mca

filename = '../../not_public/successfull_matches_1000_1010.csv'
mac = [TFF_match.initialize_mac() for i in range(8)]
mac[0] = TFF_match.match(1004, datetime.datetime(2006,11,1,13,30,0), \
                            'Lig B Kademe (Profesyonel Takım)', \
                            17960, 'METİN KIR', 17774, 'HASAN KÖLEMEN', \
                            20747, 'KAHRAMAN MİNNET', 19531, 'VEDAT ATAMAN', \
                            52,'18 MART', 137, 'DARDANELSPOR A.Ş.', \
                            131, 'İNEGÖLSPOR', 2, 1)
mac[1] = TFF_match.match(1002, datetime.datetime(2006,10,30,18,0,0), \
                            'Türk Telekom  Lig  A (Profesyonel Takım)', \
                            18902, 'SİNAN CEM İYİHUYLU', \
                            19963, 'ÖMER FARUK YEŞİL', 20144, 'MUSTAFA SÖNMEZ', \
                            19021, 'İLKER MERAL', 110, 'ATATÜRK OLİMPİYAT', \
                            3665, 'BÜYÜKŞEHİR BLD.SPOR', 132, 'KOCAELİSPOR', \
                            2,1)
mac[2] = TFF_match.match(1005, datetime.datetime(2006,11,1,13,30,0), \
                            'Lig B Kademe (Profesyonel Takım)', \
                            19928, 'ÖZGÜR SEPİN', 18958, 'ŞENOL ERSOY', \
                            20887, 'BARAN ERASLAN', 20259, 'KUTLUHAN BİLGİÇ', \
                            201, 'YALOVA ATATÜRK', 3589, 'YALOVASPOR', \
                            3659, 'KÜÇÜKKÖYSPOR', 1, 3)
mac[3] = TFF_match.match(1006, datetime.datetime(2006,11,1,13,30,0), \
                            'Lig B Kademe (Profesyonel Takım)', \
                            20132, 'SERKAN VAROL', 20565,'SEYİTHAN TURHAN', \
                            19158, 'FERZENDE EMRE', 19709, 'KORAY TAN', \
                            12, 'ANKARA OSTİM', 5, 'ETİMESGUT ŞEKERSPOR A.Ş.', \
                            3610, 'EYÜPSPOR', 3, 0)
mac[4] = TFF_match.match(1009, datetime.datetime(2006,11,2,13,30,0), \
                            'Lig B Kademe (Profesyonel Takım)', \
                            20291, 'SERKAN ERGÜN', 19521, 'GÖKHAN YAVUZ', \
                            20442, 'OKTAY ÖNGE', 20294, 'SERHAD ÜRKMEZ', \
                            112, 'BUCA İLÇE', 109, 'BUCASPOR',
                            59, 'MARMARİS BLD.GENÇLİKSPOR', 3, 1)
mac[5] = TFF_match.match(1007, datetime.datetime(2006,11,1,13,30,0), \
                            'Lig B Kademe (Profesyonel Takım)', \
                            18870, 'SACİT KEŞKEK', \
                            19973, 'MEHMET AYBERK ALTUNAY', \
                            20799, 'VOLKAN PANGAL', 20113, 'ARDA ÖZYILDIRIM', \
                            95, 'MİMAR YAHYA BAŞ', \
                            3618, 'GÜNGÖREN BELEDİYESPOR', \
                            3611, 'F.KARAGÜMRÜK', 1, 0)
mac[6] = TFF_match.match(1010, datetime.datetime(2006,11,2,13,30,0), \
                            'Lig B Kademe (Profesyonel Takım)', \
                            19381, 'MESUT CARIK', 19630, 'MEHMET GONCA', \
                            20865, 'OKTAY TAŞ', 20417, 'ÖNDER YILMAZ', \
                            149, 'MUĞLA ATATÜRK', 82, 'MUĞLASPOR', \
                            107, 'İZMİRSPOR', 1, 0)
mac[7] = TFF_match.match(1008, datetime.datetime(2006,11,1,13,30,0), \
                            'Lig B Kademe (Profesyonel Takım)', \
                            19149, 'MUSTAFA YILMAZ', 19761, 'İDRİS DAĞLI', \
                            20458, 'MEHMET ÖZÇALIŞKAN', 19678, 'DENİZ DEVECİ', \
                            48, 'OYAK RENAULT STADI', 3922, 'OYAK RENAULTSPOR', \
                            3602, 'SARIYER', 1, 2)

def test_create_match_from_csv_row():
    with open(filename, 'r') as csv_file:
        cvs_reader = csv.reader(csv_file, delimiter=',')
        headers = next(cvs_reader)
        assert mac == [mca.create_match_from_csv_row(row) for row in cvs_reader]
        
def read_and_assert(func_handle, attr_source):
    with open(filename, 'r') as csv_file:
        cvs_reader = csv.reader(csv_file, delimiter=',')
        headers = next(cvs_reader)
        x =  [func_handle(row) for row in cvs_reader]
        for i in range(len(mac)):
            assert x[i] == getattr(mac[i], attr_source)

def test_get_datetime_from_csv_row():
    read_and_assert(mca.get_datetime_from_csv_row, 'datetime')

def test_get_organizasyon_name_from_csv_row():
    read_and_assert(mca.get_organizasyon_name_from_csv_row, 'organizasyon_name')

def test_get_hakem_id_from_csv_row():
    read_and_assert(mca.get_hakem_id_from_csv_row, 'hakem_id')

def test_get_hakem_name_from_csv_row():
    read_and_assert(mca.get_hakem_name_from_csv_row, 'hakem_name')

def test_get_ar1_id_from_csv_row():
    read_and_assert(mca.get_ar1_id_from_csv_row, 'ar1_id')

def test_get_ar1_name_from_csv_row():
    read_and_assert(mca.get_ar1_name_from_csv_row, 'ar1_name')

def test_get_ar2_id_from_csv_row():
    read_and_assert(mca.get_ar2_id_from_csv_row, 'ar2_id')

def test_get_ar2_name_from_csv_row():
    read_and_assert(mca.get_ar2_name_from_csv_row, 'ar2_name')

def test_get_dort_id_from_csv_row():
    read_and_assert(mca.get_dort_id_from_csv_row, 'dort_id')

def test_get_dort_name_from_csv_row():
    read_and_assert(mca.get_dort_name_from_csv_row, 'dort_name')

def test_get_stad_id_from_csv_row():
    read_and_assert(mca.get_stad_id_from_csv_row, 'stad_id')

def test_get_stad_name_from_csv_row():
    read_and_assert(mca.get_stad_name_from_csv_row, 'stad_name')

def test_get_home_team_id_from_csv_row():
    read_and_assert(mca.get_home_team_id_from_csv_row, 'home_team_id')

def test_get_home_team_name_from_csv_row():
    read_and_assert(mca.get_home_team_name_from_csv_row, 'home_team_name')

def test_get_away_team_id_from_csv_row():
    read_and_assert(mca.get_away_team_id_from_csv_row, 'away_team_id')

def test_get_away_team_name_from_csv_row():
    read_and_assert(mca.get_away_team_name_from_csv_row, 'away_team_name')

def test_get_home_team_skor_from_csv_row():
    read_and_assert(mca.get_home_team_skor_from_csv_row, 'home_team_skor')

def test_get_away_team_skor_from_csv_row():
    read_and_assert(mca.get_away_team_skor_from_csv_row, 'away_team_skor')
