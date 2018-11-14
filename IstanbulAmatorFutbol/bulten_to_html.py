import bulten_tools as bt

def create_efso_html():
    all_bulten_filenames = bt.get_bulten_filenames()
    bulten_html_foldername = bt.get_bulten_html_foldername()
    efso_html_filename = bulten_html_foldername + '/efsolar.html'
    efso_list = bt.get_efso_list()

    with open(efso_html_filename, 'w') as myFile:
        myFile.write('<html>')
        myFile.write('<body>')
        myFile.write('<br>')
        for hakem in efso_list:
            myFile.write('<br>')
            myFile.write('<br>')
            myFile.write('EFSO HAKEM: ' + hakem)
            myFile.write('<table  border="1">')
            myFile.write('<td>Gun</td>')
            myFile.write('<td>Stad</td>')
            myFile.write('<td>Saat</td>')
            myFile.write('<td>Ev sahibi</td>')
            myFile.write('<td>Deplasman</td>')
            myFile.write('<td>Lig</td>')
            myFile.write('<td>Grup</td>')
            myFile.write('<td>Hakem</td>')
            myFile.write('<td>1. Yardimci</td>')
            myFile.write('<td>2. Yardimci</td>')
            myFile.write('<td>4. Hakem</td>')
            myFile.write('<td>Gozlemci</td>')
            for bulten_filename in all_bulten_filenames:
                match_list = bt.get_matches(bulten_filename)
                for mac in match_list:
                    if bt.is_this_an_efso_mac(hakem, mac):
                        myFile.write('<tr>')
                        myFile.write('<td>'+mac.date+'</td>')
                        myFile.write('<td>'+mac.place+'</td>')
                        myFile.write('<td>'+mac.time+'</td>')
                        myFile.write('<td>'+mac.home+'</td>')
                        myFile.write('<td>'+mac.away+'</td>')
                        myFile.write('<td>'+mac.league+'</td>')
                        myFile.write('<td>'+mac.group+'</td>')
                        myFile.write('<td>'+mac.ref+'</td>')
                        myFile.write('<td>'+mac.ar1+'</td>')
                        myFile.write('<td>'+mac.ar2+'</td>')
                        myFile.write('<td>'+mac.fourth+'</td>')
                        myFile.write('<td>'+mac.observer+'</td>')
                        myFile.write('</tr>')
            myFile.write('</table>')

        myFile.write('</body>')
        myFile.write('</html>')

def create_bulten_html(week_number):
    all_bulten_filenames = bt.get_bulten_filenames()
    bulten_filename = all_bulten_filenames[week_number-1]
    week_no_str = bt.get_bulten_week_number_as_str(bulten_filename)
    match_list = bt.get_matches(bulten_filename)
    bulten_html_foldername = bt.get_bulten_html_foldername()
    bulten_html_filename = bulten_html_foldername + '/' + \
                                f'bulten_{week_no_str}.html'

    with open(bulten_html_filename, 'w') as myFile:
        myFile.write('<html>')
        myFile.write('<body>')
        myFile.write('<br>')
        myFile.write('HAFTA: '+week_no_str)
        myFile.write('<br>')

        myFile.write('<table  border="1">')
        myFile.write('<td>Gun</td>')
        myFile.write('<td>Stad</td>')
        myFile.write('<td>Saat</td>')
        myFile.write('<td>Ev sahibi</td>')
        myFile.write('<td>Deplasman</td>')
        myFile.write('<td>Lig</td>')
        myFile.write('<td>Grup</td>')
        myFile.write('<td>Hakem</td>')
        myFile.write('<td>1. Yardimci</td>')
        myFile.write('<td>2. Yardimci</td>')
        myFile.write('<td>4. Hakem</td>')
        myFile.write('<td>Gozlemci</td>')
        for mac in match_list:
            myFile.write('<tr>')
            myFile.write('<td>'+mac.date+'</td>')
            myFile.write('<td>'+mac.place+'</td>')
            myFile.write('<td>'+mac.time+'</td>')
            myFile.write('<td>'+mac.home+'</td>')
            myFile.write('<td>'+mac.away+'</td>')
            myFile.write('<td>'+mac.league+'</td>')
            myFile.write('<td>'+mac.group+'</td>')
            myFile.write('<td>'+mac.ref+'</td>')
            myFile.write('<td>'+mac.ar1+'</td>')
            myFile.write('<td>'+mac.ar2+'</td>')
            myFile.write('<td>'+mac.fourth+'</td>')
            myFile.write('<td>'+mac.observer+'</td>')
            myFile.write('</tr>')
        myFile.write('</table>')

        myFile.write('</body>')
        myFile.write('</html>')
