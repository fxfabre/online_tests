from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        players = list(self.standings.keys())
        players.sort(key=lambda pl:(
            -self.standings[pl]["score"],
            self.standings[pl]['games_played'],
            list(self.standings.keys()).index(pl)
        ))
        return players[rank - 1]
        
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)

print(table.player_rank(1))



