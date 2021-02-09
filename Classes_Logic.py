class GameEntry:

    def __init__(self, name, score = 0):
        self.name = name
        self.score =  score

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name



class ScoreBoard:
    def __init__(self):
        self.board =  []
    
    def __len__(self):
        return len(self.board)

    def __str__(self):
        players = [ i for i in self.board]
        return str(players)


    def add_player(self, new_player, new_score):
        player =  GameEntry(name =  new_player, score =  new_score)
        n_player = {"Name" : player.get_name(), "Score" :  player.get_score()}
        if isinstance(new_player, str) and isinstance(new_score, int):
            self.board.append(n_player)
        else:
            raise TypeError("Given Type is not valid")

    def find_player(self, player_name):
        found = [person for person in self.board if person["Name"] == player_name]
        return found


    def find_high_score(self):
        scores = sorted(self.board, key =  lambda x:x["Score"], reverse=False)
        return scores[-1]

    def has_player(self, player_name):
        while True:
            for player in range(len(self.board)):
                if self.board[player]["Name"]== player_name:
                    return True
            return False

    





my_scores =  ScoreBoard()
my_scores.add_player(new_player="Orik", new_score=2002)
my_scores.add_player(new_player="John", new_score=100)
my_scores.add_player(new_player="Anna", new_score=3002)
my_scores.add_player(new_player="Orik", new_score=3008)

