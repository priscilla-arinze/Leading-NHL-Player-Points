import requests # one of the ways to connect to websites via Python
from bs4 import BeautifulSoup # allows you to go through page source and get data
import re # regular expressions library

def indiv_nhl_team_abbrev(team_url):
    # GET request; stores page HTML source in variable
    source_code = requests.get(team_url) 

    # gets the front end text of the HTMl source code; ignoring back end stuff; essentally parses through HTML source
    plain_text = source_code.text 

    # can sort through this variable
    soup = BeautifulSoup(plain_text) 


    # on the individual team page, targeting the orange highlighted cell under the standings section, then getting team
    standings_highlighted_cell = soup.find('tr', {'class': 'covers-CoversMatchups-teamPosHighlight'})

    #team_initials = standings_highlighted_cell.find('td')

    return standings_highlighted_cell.get_text()

indiv_nhl_team_abbrev('https://www.covers.com/sport/hockey/nhl/teams/main/boston-bruins/teamstats')