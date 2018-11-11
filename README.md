# NFL_Scripts

This repo is a project to query NFL stats that I'm interested in, mostly used for personal Fantasy Football analysis.

Stats may not be 100% accurate, but data is pulled directly from ESPN through [nflgame](https://github.com/BurntSushi/nflgame)repository.
<br />A more recent version of nflgame project is maintained at this [fork](https://github.com/derek-adair/nflgame).

`player_scripts.py` prints players at top of current position (by several stats) for current season or specified week(s).
<br />I can use this for waiver claims or making decisions on which players have done well.

`team_scripts.py` contains functions which print team level stats such as most rushing or receiving yards for a team, or yards gained against a team
I can use this to determine which players will likely do well against a certain matchup, or if which defense matchups are likely to perform.

Example of player_scripts:
```
>>> import player_scripts as p
>>> p.print_top_rushers_by_ben(5)


Best Rushers:
1  T.Gurley         LA   A:187  Y:897   AVG:4
2  J.Conner         PIT  A:164  Y:771   AVG:4
3  K.Hunt           KC   A:167  Y:754   AVG:4
4  E.Elliott        DAL  A:149  Y:680   AVG:4
5  A.Peterson       WAS  A:155  Y:672   AVG:4
```


Example of team_scripts:

```
>>> import team_scripts as t
>>> t.print_worst_rushing_def()
CLE has allowed 1404 rushing yds
MIA has allowed 1396 rushing yds
ARI has allowed 1357 rushing yds
CIN has allowed 1305 rushing yds
...
```
