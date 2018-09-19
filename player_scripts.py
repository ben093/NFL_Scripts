#!python
import nflgame


def rushing_yards_leaders(year=0,week=0,num=5):
	if year == 0 and week == 0:
		year, week = nflgame.live.current_year_and_week()
	
	print "For year %d, week %d:" % (year, week)	
	games = nflgame.games(year, week)
	players = nflgame.combine_game_stats(games)
	
	for p in players.rushing().sort('rushing_yds').limit(num):
		msg = '%s %d carries for %d yards and %d TDs'
		print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)



def top_receiving_targets_this_season():
	year, current_week = nflgame.live.current_year_and_week()
	weeks = [x for x in range(1, current_week+1)]

	games = nflgame.games(year, weeks)
	players = nflgame.combine(games, plays=True)

	print "\n\Targets:"
	for p in players.sort('receiving_tar').limit(50):
		print p, p.receiving_tar
		
def top_receivers_by_ben():		
	year, current_week = nflgame.live.current_year_and_week()
	weeks = [x for x in range(1, current_week+1)]

	games = nflgame.games(year, weeks)
	players = nflgame.combine(games, plays=True)

	stars = [[None,None,None,None]]
	
	#print "\nStars:"
	for p in players.sort('receiving_tar').limit(50):
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
			
def top_rushers_by_ben():
	year, current_week = nflgame.live.current_year_and_week()
	weeks = [x for x in range(1, current_week+1)]

	games = nflgame.games(year, weeks)
	players = nflgame.combine(games, plays=True)

	stars = [[None,None,None,None]]
	
	print "\nStars:"
	for p in players.sort('rushing_yds').limit(50):
		print p, p.team, p.rushing_att, p.rushing_yds
		player = p, p.team, p.rushing_att, p.rushing_yds
		stars.append(player)

	print "\n\nBest Rushers: "
	count = 1
	for p in stars:
		if p[0] != None:
			#print "%d. %s targets: %d times for a total of %d cmplts and %d yards." % (count, p[0], p[1], p[2], p[3])
			name = p[0]
			team = p[1]
			attempts = p[2]
			yards = p[3]
			avg_yds_carry = int((float(yards) / attempts));
			print "{0:<2} {1:<16} {2:<3}  A:{3:<4} Y:{4:<5} AVG:{5:<2}".format(count, name, team, attempts, yards, avg_yds_carry)
			count+=1

		
def top_receivers_by_benB():
	year, current_week = nflgame.live.current_year_and_week()
	weeks = [x for x in range(1, current_week+1)]

	games = nflgame.games(year, weeks)
	players = nflgame.combine(games, plays=True)
	
	# 2 Lists
	targets = [[None,None]]
	yards = [[None,None]]
	
	print "\nTargets:"
	for p in players.sort('receiving_tar').limit(50):
		print p, p.receiving_tar
		player = p, p.receiving_tar
		targets.append(player)
		
	print "\n\nYards:"
	for p in players.sort('receiving_yds').limit(50):
		print p, p.receiving_yds
		player = p, p.receiving_yds
		yards.append(player)
		
	'''print "\n\nReceptions"
	for p in players.sort('receiving_rec').limit(50):
		print p, p.receiving_rec
		player = p, p.receiving_rec
		yards.append(player)'''	
	
	# Find matches
	stars = [[ x[0], x[1], y[1] ] for x in targets for y in yards if x[0] == y[0]]
	
	print "\n\nBest Players: "
	count = 1
	for p in stars:
		if p[0] != None:
			print "%d. %s was targeted %d times for a total of %d yards." % (count, p[0], p[1], p[2])
			count+=1
