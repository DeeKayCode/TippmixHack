from datetime import datetime, time, date
from bs4 import BeautifulSoup
from urllib import request


#Input manager
def getMatchWithDate(homeTeam, awayTeam, userInput=str(date.today()), url='https://fbref.com/en/matches/'):
    url = url + userInput
    soup = BeautifulSoup(request.urlopen(url), 'html.parser')
    allTables = soup.find_all('table')
    for table in allTables:
        if 'stats_table' in table['class']:
            allRows = table.tbody.find_all('tr')
            matchRow = None
            for row in allRows:
                #print(row.prettify())
                allTds = row.find_all('td')
                homeTeamRow = None
                awayTeamRow = None
                for td in allTds:
                    if str(td['data-stat']) == 'squad_a' and td.a.string == homeTeam:
                        homeTeamRow = row
                    if str(td['data-stat']) == 'squad_b' and td.a.string == awayTeam:
                        awayTeamRow = row
                    #If match found
                    if homeTeamRow == awayTeamRow and homeTeamRow != None:
                        matchRow = row
                        return matchRow


print(getMatchWithDate('Diósgyőr', 'Mezőkövesd', '2020-05-30'))