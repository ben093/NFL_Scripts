import nflgame

isDebug = False
 
# FOR A TEAM   
def get_receiving_yds(seas, week, team):
    '''
    This will return a teams receiving yards for a specific season and week.
    '''
    games = nflgame.games_gen(seas, week, team, team)
    if games == None:
        # Catch all for teams that have moved or joined the league.      
        return team, 0
    plays = nflgame.combine_plays(games)

    yds = 0
    for p in plays.filter(team=team,receiving_yds__ge=1):
        if isDebug:
            print p
        yds += p.receiving_yds
    return team, yds
  
def get_rec_yds_per_team(season=None, weeks=None):
    '''
    This returns all teams receiving yards for a season and week(s)
    '''
    if season == None and weeks == None:
        season, current_week = nflgame.live.current_year_and_week()
        weeks = [x for x in range(1, current_week+1)]
    
    nfl_teams = nflgame.teams
    team_rec_yds = []
        
    for team in nfl_teams:
        team_abbrev = nflgame.standard_team(team[0])        
        result = get_receiving_yds(season, weeks, team_abbrev)               
        
        if (result[1] > 0): 
            # Only teams with receiving yards
            if isDebug:
                print "%s had %s receiving yds" % (result[0], result[1])
            team_rec_yds.append(result)
    
    # Return list of teams and receiving yds
    return team_rec_yds

def print_best_passing_off():
    '''
    Prints the 'best' passing offense by teams receiving yards.
    '''
    results = get_rec_yds_per_team()
    results.sort(key = lambda x: (x[1]), reverse=True)
    
    for x in results:
        print "%s has %s receiving yds" % (x[0], x[1])

def get_rushing_yds(seas, week, team):
    '''
    This will return a teams receiving yards for a specific season and week.
    '''
    games = nflgame.games_gen(seas, week, team, team)
    if games == None:
        # Catch all for teams that have moved or joined the league.      
        return team, 0
    plays = nflgame.combine_plays(games)

    yds = 0
    for p in plays.filter(team=team,rushing_yds__ge=1):
        if isDebug:
            print p
        yds += p.rushing_yds
    return team, yds

def get_rush_yds_per_team(season=None, weeks=None):
    '''
    This returns all teams receiving yards for a season and week(s)
    '''
    if season == None and weeks == None:
        season, current_week = nflgame.live.current_year_and_week()
        weeks = [x for x in range(1, current_week+1)]
    
    nfl_teams = nflgame.teams
    team_rec_yds = []
        
    for team in nfl_teams:
        team_abbrev = nflgame.standard_team(team[0])        
        result = get_rushing_yds(season, weeks, team_abbrev)               
        
        if (result[1] > 0): 
            # Only teams with receiving yards
            if isDebug:
                print "%s had %s rushing yds" % (result[0], result[1])
            team_rec_yds.append(result)
    
    # Return list of teams and receiving yds
    return team_rec_yds

def print_best_rushing_off():
    '''
    Prints the 'best' passing offense by teams receiving yards.
    '''
    results = get_rush_yds_per_team()
    results.sort(key = lambda x: (x[1]), reverse=True)
    
    for x in results:
        print "%s has %s rushing yds" % (x[0], x[1])
    
# END FOR A TEAM
        
# AGAINST TEAM        
def get_receiving_yds_against(seas, week, team):
    '''
    Returns a tuple containing a team and receiving yards against said team for season and week(s)
    '''
    games = nflgame.games_gen(seas, week, team, team)
    if games == None:
        # Catch all for teams that have moved or joined the league. 
        return team, 0
    plays = nflgame.combine_plays(games)

    yds = 0
    for p in plays.filter(team__ne=team,receiving_yds__ge=1):
        yds += p.receiving_yds
    return team, yds
        
def get_rec_yds_against_per_team(season=None, weeks=None):
    '''
    Returns a list of all teams and receiving yards scored against them (with at least 1 yard)
    '''
    if season == None and weeks == None:
        season, current_week = nflgame.live.current_year_and_week()
        weeks = [x for x in range(1, current_week+1)]   
    nfl_teams = nflgame.teams
        
    team_yds_against = []
    
    for team in nfl_teams:
        team_abbrev = nflgame.standard_team(team[0])        
        result = get_receiving_yds_against(season, weeks, team_abbrev)
        
        if (result[1] > 0): 
            # Only teams with yards against
            if isDebug:
                print "%s gave up %s passing yds" % (result[0], result[1])
            team_yds_against.append(result)
    # Return list of receiving yds scored against this team
    return team_yds_against
    
def print_worst_passing_def():
    '''
    Prints the team with most receiving yards scored against them.
    '''
    results = get_rec_yds_against_per_team()
    results.sort(key = lambda x: (x[1]),reverse=True)

    for x in results:
        print "%s has allowed %s receiving yds" % (x[0], x[1])

def get_rushing_yds_against(seas, week, team):
    '''
    Returns a tuple containing a team and receiving yards against said team for season and week(s)
    '''
    games = nflgame.games_gen(seas, week, team, team)
    if games == None:
        # Catch all for teams that have moved or joined the league. 
        return team, 0
    plays = nflgame.combine_plays(games)

    yds = 0
    for p in plays.filter(team__ne=team,rushing_yds__ge=1):
        yds += p.rushing_yds
    return team, yds

def get_rush_yds_against_per_team(season=None, weeks=None):
    '''
    Returns a list of all teams and receiving yards scored against them (with at least 1 yard)
    '''
    if season == None and weeks == None:
        season, current_week = nflgame.live.current_year_and_week()
        weeks = [x for x in range(1, current_week+1)]   
    nfl_teams = nflgame.teams
        
    team_yds_against = []
    
    for team in nfl_teams:
        team_abbrev = nflgame.standard_team(team[0])        
        result = get_rushing_yds_against(season, weeks, team_abbrev)
        
        if (result[1] > 0): 
            # Only teams with yards against
            if isDebug:
                print "%s gave up %s rushing yds" % (result[0], result[1])
            team_yds_against.append(result)
    # Return list of receiving yds scored against this team
    return team_yds_against

def print_worst_rushing_def():
    '''
    Prints the team with most receiving yards scored against them.
    '''
    results = get_rush_yds_against_per_team()
    results.sort(key = lambda x: (x[1]),reverse=True)

    for x in results:
        print "%s has allowed %s rushing yds" % (x[0], x[1])
    
# END AGAINST TEAM