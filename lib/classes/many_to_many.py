class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, 'title'):
            raise Exception
        else:
            if isinstance(title, str) and len(title) > 0:
                self._title = title
            else:
                raise Exception

    def results(self, result=None):
        if isinstance(result, Result):
            self._results.append(result)
        return self._results
        
    def players(self, player=None):
        if isinstance(player, Player) and player not in self._players:
            self._players.append(player)
        return self._players

    def average_score(self, player):
        player_results = []
        for result in self._results:
            if result.player == player:
                player_results.append(result.score)
            
        return sum(player_results) / len(player_results)

class Player:
    def __init__(self, username):
        self.username = username
        self._results = []
        self._games = []
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else: 
            raise Exception

    def results(self, result=None):
        if isinstance(result, Result):
            self._results.append(result)
        return self._results

    def games_played(self, game=None):
        if isinstance(game, Game) and game not in self._games:
            self._games.append(game)
        return self._games

    def played_game(self, game):
        return game in self._games

    def num_times_played(self, game):
        return sum(1 for result in self._results if result.game == game)

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        game.results(self)
        game.players(player)
        player.results(self)
        player.games_played(game)
        Result.all.append(self)
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, 'score'):
            raise Exception
        else: 
            if isinstance(score, int) and 1 <= score <= 5000:
                self._score = score 

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = Game