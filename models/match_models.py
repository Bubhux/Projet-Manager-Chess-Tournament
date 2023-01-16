"""Définie les matchs."""

#from models.player_models import Player
from views.view_user_entry import ViewUserEntry


class Match:
    """Match."""

    MATCH_NUMBER = 1

    def __init__(self, name, pairs_players, player_1=None, player_2=None, score_player_1=0, score_player_2=0):
        """Initialise la paire de joueurs, le score de chaque joueurs."""
        #self.name = "Match" + str(Match.MATCH_NUMBER)
        self.name = name
        self.player_1 = player_1
        self.player1 = pairs_players[0]
        self.player_2 = player_2
        self.player2 = pairs_players[1]
        #self.pairs_players = pairs_players
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.winner = ""

    def __repr__(self):
        return ([self.player1, self.score_player_1],
                [self.player2, self.score_player_2])
    
    #def __str__(self):
        """Indique le numéro du match et les joueurs qui vont s'affronter."""
        #return f"{self.name} : {self.player1} --VS-- {self.player2}"

    #def __repr__(self):
        """Indique le numéro du match et les joueurs qui vont s'affronter."""
        #return f"{self.name} : {self.player1} --VS-- {self.player2}"

    """
    def create_match(self):
        matchs = []
        for i, pair in enumerate(self.pairs_players):
            matchs.append(Match(name=f"Match {i}", pairs_players=pair))
        return matchs
    """
    def match_played(self):

        winner = ViewUserEntry().user_entry(
            message_display=f"{self.player1.name} --VS-- " + f"{self.player2.name}\n"
                            f"Sélectionner le gagnant\n"
                            f"1 - {self.player1.name}\n"
                            f"2 - {self.player2.name}\n"
                            f"3 - Égalité\n> ",
            message_error="Sélectionner 1, 2 ou 3",
            value_type="Sélection",
            assertions=["1", "2", "3"]
        )

        if winner == "1":
            self.winner = self.player1.name
            self.score_player_1 += 1 
        elif winner == "2":
            self.winner = self.player2.name
            self.score_player_2 += 1
        elif winner == "3":
            self.winner = "Égalité"
            self.score_player_1 += 0.5
            self.score_player_2 += 0.5

        self.player1.tournament_score += self.score_player_1
        self.player2.tournament_score += self.score_player_2

    """
    def match_completed(self):
        self.date_end = display_check_timestamp()
        print(f"{self.date_end} : {self.name} terminé ")
        print("Rentrer les résultats des matchs : ")
        for match in self.matchs:
            match.match_played()
    """

    def serialized_match(self):
        return {
            "player1": self.player1.serialized_player(save_tournament_score=True),
            "score_player_1": self.score_player_1,
            "player2": self.player2.serialized_player(save_tournament_score=True),
            "score_player_2": self.score_player_2,
            "winner":self.winner,
            "name": self.name,
        }

