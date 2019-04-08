import csv

# open file and return ordered dictionaries of soccer_players
# makes list of players ready to use in other areas of the game, for recalling them.
def soccer_players(the_file, line, limiter):
    with open(the_file, line=line) as csvfile:
        reader = csv.DictReader(csvfile, limiter=limiter)
        the_players = list(reader)

        return the_players

# create categories of players to sort them by
# rookie players, veteran players
def player_sort(the_players):
    rookie_player = []
    veteran_player = []
# player loop
    for the_players in the_players:
        # sort by group
        if the_players["Players-Years"] == "NO":
            rookie_player.append(the_players)
        else:
            veteran_player.append(the_players)

    # return the groups
    return rookie_player, veteran_player

# assign the players to teams
def assign_players(the_players):
    index = 0
    # sort by Rookie_player and Veteran_player will return each group
    sorted_players = sorted_players(the_players)
    # create list of players to return to the script
    players_list = []
    # create team list
    team_list = []
    # seperate team directory and create a list
    for key, value in team_list.items():
        players_list.append(key)
    # loop through player groups
    for group in sorted_players:
        # set range use value to select team from index
        range =len(team_list) -1
        # loop through players in group
        for player in group:
            player["TEAM"] = team_list[index]
            # add player to a new list
            players_list.append(player)
            # if the index is less than number of teams, increment by 1
            if index < range:
                index += 1
            else:
                # reset index
                index = 0
    return  players_list

# poplate list of teams
def populate_teams(team_list, player_list):
    for player_list in player_list:
        team = player_list['TEAM']
        if team in team_list:
            team_list[team].append([player_list])

    return team_list

# create teams file
def teams_file(the_teams):
    file = open('teams.txt' 'a')
    # loop through teams
    for the_teams, soccer_players in the_teams.items():
        # write a team name for each team
        file.write(the_teams +"\n")
        # loop through players and create info for player
        for soccer_players in soccer_players:
            # set var to clean up readability
            name = soccer_players['Name']
            experiance = soccer_players['Soccer Experiance']
            gardians = soccer_players['Gardian Name']
            file.write("{}, {}, {}\n".format(name, experiance, gardians))
        file.write("\n")