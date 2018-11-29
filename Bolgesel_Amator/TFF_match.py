#!/usr/bin/#!/usr/bin/env python3
from datetime import datetime
default_datetime = datetime(2000,1,1,0,0,0)

def initialize_mac():
    return match(0, default_datetime, '', 0, '', 0, '', 0, '', 0, '', \
                    0, '', '', 0, '', 0, 0, 0)

class match():
    def __init__(self, mac_id, \
                        datetime, \
                        organizasyon_name, \
                        hakem_id, hakem_name, \
                        ar1_id, ar1_name, ar2_id, ar2_name, \
                        dort_id, dort_name, \
                        stad_id, stad_name, \
                        home_team_id, home_team_name, \
                        away_team_id, away_team_name, \
                        home_team_skor, away_team_skor):
        self.mac_id = mac_id
        self.stad_id, self.stad_name = stad_id, stad_name

        self.hakem_id, self.hakem_name = hakem_id, hakem_name
        self.ar1_id, self.ar1_name = ar1_id, ar1_name
        self.ar2_id, self.ar2_name = ar2_id, ar2_name
        self.dort_id, self.dort_name = dort_id, dort_name

        self.datetime = datetime
        self.organizasyon_name = organizasyon_name

        self.home_team_id, self.home_team_name = home_team_id, home_team_name
        self.away_team_id, self.away_team_name = away_team_id, away_team_name

        self.home_team_skor = home_team_skor
        self.away_team_skor = away_team_skor

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def all_info_in_one_line(self):
        # backup = f"{self.mac_id},{self.datetime},{self.organizasyon_name},{self.hakem_id},{self.hakem_name},{self.ar1_id},{self.ar1_name},{self.ar2_id},{self.ar2_name},{self.dort_id},{self.dort_name},{self.stad_id},{self.stad_name},{self.home_team_id},{self.home_team_name},{self.away_team_id},{self.away_team_name},{self.home_team_skor},{self.away_team_skor}"
        return str(self.mac_id) + ',' + str(self.datetime) + ',' + \
                self.organizasyon_name + ',' + \
                str(self.hakem_id) + ',' + self.hakem_name + ',' + \
                str(self.ar1_id) + ',' + self.ar1_name + ',' + \
                str(self.ar2_id) + ',' + self.ar2_name + ',' + \
                str(self.dort_id) + ',' + self.dort_name + ',' + \
                str(self.stad_id) + ',' + self.stad_name + ',' + \
                str(self.home_team_id) + ',' + self.home_team_name + ',' + \
                str(self.away_team_id) + ',' + self.away_team_name + ',' + \
                str(self.home_team_skor) + ',' + str(self.away_team_skor)

    def print_summary(self):
        header = '[' + 'TFF match #' + str(self.mac_id) + ']'
        print(header, self.datetime)
        print(header, self.hakem_name, ',', \
                        self.ar1_name, ',', self.ar2_name, ',', self.dort_name)
        print(header, self.home_team_name, self.home_team_skor, '-', \
                        self.away_team_skor, self.away_team_name)
