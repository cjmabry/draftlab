import nflgame
"""Parse NFL play-by-play data for passes by distance and side of field
"""

team_name = 'TEN'
year = 2015
kind = 'REG'

games = nflgame.games(year=year, kind=kind, home=team_name, away=team_name)



pass_play_count = 0
short_right = 0
short_middle = 0
short_left = 0
deep_right = 0
deep_middle = 0
deep_left = 0

for game in games:
    for drive in game.drives:
        for play in drive.plays:
                play_string = str(play)

                if play_string[0] == '(':

                    # get the team name from the play
                    team = play_string.split('(')[1].split(',')[0]

                    if team == team_name:

                        if 'pass' in play_string:
                            pass_play_count += 1

                            if 'short right' in play_string:
                                short_right += 1

                            if 'short middle' in play_string:
                                short_middle += 1

                            if 'short left' in play_string:
                                short_left += 1

                            if 'deep right' in play_string:
                                deep_right += 1

                            if 'deep middle' in play_string:
                                deep_middle += 1

                            if 'deep left' in play_string:
                                deep_left += 1

print('Team: ' + team_name)
print('Short right pass attempts: ' + str(short_right))
print('Short middle pass attempts: ' + str(short_middle))
print('Short left pass attempts: ' + str(short_left))
print('Deep right pass attempts: ' + str(deep_right))
print('Deep middle pass attempts: ' + str(deep_middle))
print('Deep left pass attempts: ' + str(deep_left))
