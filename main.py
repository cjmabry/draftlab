import json, csv, nflgame, gspread
from xml.etree import ElementTree
from collections import OrderedDict
from pprint import pprint
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('Fantasy Stats-ec2a54ddd87a.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

gc = gspread.authorize(credentials)

sh = gc.open('Week 3 Fantasy Sheet')

positions = OrderedDict((("WR",[]), ("TE",[]), ("DST",[]) ))

worksheet_list = sh.worksheets()

with open('DKSalaries.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        position = str(row[0])
        if position != 'Position' and position != 'QB' and position != 'RB':
            positions[row[0]].append(row)

for key, value in positions.iteritems():
    worksheet = sh.add_worksheet(title=key, rows='200', cols='20')
    worksheet.update_cell(1,1,'Position')
    worksheet.update_cell(1,2,'Name')
    worksheet.update_cell(1,3,'Salary')
    worksheet.update_cell(1,4,'Game')
    worksheet.update_cell(1,5,'FPPG')
    worksheet.update_cell(1,6,'Team')
    worksheet.update_cell(1,7,'Opponent')
    worksheet.update_cell(1,8,'Home/Away')
    worksheet.update_cell(1,9,'Opp Pa Yds Allowed')
    worksheet.update_cell(1,10,'Opp Pa TDs Allowed')
    worksheet.update_cell(1,11,'Opp Ru Yds Allowed')
    worksheet.update_cell(1,12,'Opp Ru TDs Allowed')
    worksheet.update_cell(1,13,'Spread')

    for idx, row in enumerate(value):
        team = nflgame.standard_team(row[5])
        home_team = nflgame.standard_team(row[3].split(" ")[0].split("@")[1])
        away_team = nflgame.standard_team(row[3].split(" ")[0].split("@")[0])

        if team == home_team:
            opponent = away_team
            row.append(opponent)
            row.append('Home')

        elif team == away_team:
            opponent = home_team
            row.append(opponent)
            row.append('Away')

        games = nflgame.games(2015, home=opponent, away=opponent, kind='REG')

        passing_yards_allowed = 0
        passing_tds_allowed = 0
        rushing_yards_allowed = 0
        rushing_tds_allowed = 0

        for game in games:
            if opponent == game.home:
                passing_yards_allowed += game.stats_away.passing_yds
                rushing_yards_allowed += game.stats_away.rushing_yds
                scores = game.scores

                for score in scores:
                    if 'pass' in score and 'TD' in score and game.away in score:
                        passing_tds_allowed += 1
                    if 'run' in score and 'TD' in score and game.away in score:
                        rushing_tds_allowed += 1

            elif opponent == game.away:
                passing_yards_allowed += game.stats_home.passing_yds
                rushing_yards_allowed += game.stats_home.rushing_yds


                scores = game.scores

                for score in scores:
                    if 'pass' in score and 'TD' in score and game.home in score:
                        passing_tds_allowed += 1
                    if 'run' in score and 'TD' in score and game.home in score:
                        rushing_tds_allowed += 1

        row.append(passing_yards_allowed)
        row.append(passing_tds_allowed)
        row.append(rushing_yards_allowed)
        row.append(rushing_tds_allowed)

        # odds
        tree = ElementTree.parse('pinnaclefeed.aspx.xml')
        root = tree.getroot()

        events = root[3]

        events = root.findall("./events/event")

        for thing in events:

            participants = thing.findall("./participants/participant/participant_name")

            for participant in participants:
                team_name = participant.text
                if nflgame.standard_team(team_name) is not None:
                    team_name = nflgame.standard_team(team_name)
                    if team_name == team:

                        if team == home_team:
                            if thing.find("./periods/period/spread/spread_home") is not None:
                                spread = thing.find("./periods/period/spread/spread_home").text
                                row.append(spread)
                        elif team == away_team:
                            if thing.find("./periods/period/spread/spread_visiting") is not None:
                                spread = thing.find("./periods/period/spread/spread_visiting").text
                                row.append(spread)

        for pos, thing in enumerate(row):
            worksheet.update_cell(idx + 2, pos + 1, thing)

# for thing in positions:
    # worksheet = sh.add_worksheet(title=thing, rows='100', cols='20')
    # worksheet.update_cell()
