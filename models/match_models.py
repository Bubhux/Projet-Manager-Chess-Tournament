"""Définie les matchs."""

from models.player_models import Player
from views.view_user_entry import display_check_timestamp


class Match:
    """Match."""

    MATCH_NUMBER = 1

    def __init__(self, name, player_1, player_2, pairs_players, score_player_1=0, score_player_2=0):
        """Initialise la paire de joueurs, le score de chaque joueurs."""
        self.name = "Match" + str(Match.MATCH_NUMBER)
        self.player_1 = player_1
        self.player_2 = player_2
        self.pairs_players = pairs_players
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __str__(self):
        """Indique le numéro du match et les joueurs qui vont s'affronter."""
        return f"{self.name} : {self.player_1} --VS-- {self.player_2}"

    def __repr__(self):
        """Indique le numéro du match et les joueurs qui vont s'affronter."""
        return f"{self.name} : {self.player_1} --VS-- {self.player_2}"

    def create_match(self):
    	matchs = []
    	for i, pair in enumerate(self.pairs_players):
    		matchs.append(Match(name=f"Match {i}", pairs_players=pair))
    	return matchs

    def match_played(self):
        if winner == "0":
            self.winner = self.player_1.name, self.player_1.surname
            self.score_player_1 += 1 
        elif winner == "1":
            self.winner = self.player_2.name, self.player_2.surname
        elif winner == "2":
            self.winner = "Égalité"
            self.score_player_1 += 0.5
            self.score_player_2 += 0.5

        self.player_1.tournament_score += self.score_player_1
        self.player_2.tournament_score += self.score_player_2

    def match_completed(self):
        self.date_end = display_check_timestamp()
        print(f"{self.date_end} : {self.name} terminé ")
        print("Rentrer les résultats des matchs : ")
        for match in self.matchs:
            match.match_played()

