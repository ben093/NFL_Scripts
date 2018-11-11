import nflgame

def top_receiving_targets_this_season():
    year, current_week = nflgame.live.current_year_and_week()
    weeks = [x for x in range(1, current_week+1)]

    games = nflgame.games(year, weeks)
    players = nflgame.combine(games, plays=True)

    print "\n\Targets:"
    for p in players.sort('receiving_tar').limit(50):
        print p, p.receiving_tar

        
def print_top_flex_by_ben(num_results=100):
    '''
    This will print players with highest combined rush/receiving attempts and 
    show stats attempts and yardage gains.
    '''
    year, current_week = nflgame.live.current_year_and_week()
    weeks = [x for x in range(1, current_week+1)]

    games = nflgame.games(year, weeks)
    players = nflgame.combine(games, plays=True)

    stars = [[]]
    
    for p in players:
        combined_yards = p.receiving_yds + p.rushing_yds
        combined_attempts = p.receiving_tar + p.rushing_att
        a_player = combined_yards, combined_attempts, p
        stars.append(a_player)
        
    stars.sort(reverse=True)
        
    print "\n\nBest Flex: "
    count = 1
    for player in stars:    
        if player != []:
            tot_yards = player[0]
            tot_attempts = player[1]
            name = player[2]
            team =  player[2].team            
            if tot_attempts != 0:                
                avg_yds_each = int((float(tot_yards) / tot_attempts));
            else: 
                avg_yds_each = 0
            print "{0:<3} {1:<16} {2:<3}  Y:{3:<5} A:{4:<4} AVG:{5:<2}".format(count, name, team, tot_yards, tot_attempts, avg_yds_each)
            count+=1    
        if count > num_results: break
        
def print_top_receivers_by_ben(num_results=50):        
    '''
    This will print players with highest targets and 
    show stats of completions and yardage gains.
    '''
    year, current_week = nflgame.live.current_year_and_week()
    weeks = [x for x in range(1, current_week+1)]

    games = nflgame.games(year, weeks)
    players = nflgame.combine(games, plays=True)

    stars = [[None]]
    
    #print "\nStars:"
    for p in players.sort('receiving_tar').limit(num_results):
        #print p, p.receiving_tar, p.receiving_rec, p.receiving_yds
        player = p, p.team, p.receiving_tar, p.receiving_rec, p.receiving_yds
        stars.append(player)

    print "\n\nBest Receivers: "
    count = 1
    for p in stars:
        if p[0] != None:
            #print "%d. %s targets: %d times for a total of %d cmplts and %d yards." % (count, p[0], p[1], p[2], p[3])
            name = p[0]
            team = p[1]
            targets = p[2]
            cmplt = p[3]
            yards = p[4]
            completion_percent = int(100*(float(cmplt) / targets));
            print "{0:<2} {1:<16} {2:<3}  T:{3:<4} R:{4:<4} Y:{5:<5} C:{6:<2}%".format(count, name, team, targets, cmplt, yards, completion_percent)
            count+=1
        
def print_top_rushers_by_ben(num_results=50, year=None, weeks=None):
    '''
    This will print players with highest rushing yards and 
    show stats of attempts and yardage gains.
    '''
    if year is None:
        year, current_week = nflgame.live.current_year_and_week()
    if weeks is None:
        unused_var, current_week = nflgame.live.current_year_and_week()
        weeks = [x for x in range(1, current_week+1)]

    games = nflgame.games(year, weeks)
    #print games
    players = nflgame.combine(games, plays=True)

    stars = [[None]]
    
    #print "\nStars:"
    for p in players.sort('rushing_yds').limit(num_results):
        #print p, p.team, p.rushing_att, p.rushing_yds
        player = p, p.team, p.rushing_att, p.rushing_yds
        stars.append(player)

    print "\n\nBest Rushers: "
    count = 1
    for p in stars:
        if p[0] != None:
            name = p[0]
            team = p[1]
            attempts = p[2]
            yards = p[3]
            avg_yds_carry = int((float(yards) / attempts));
            print "{0:<2} {1:<16} {2:<3}  A:{3:<4} Y:{4:<5} AVG:{5:<2}".format(count, name, team, attempts, yards, avg_yds_carry)
            count+=1
