"""Module match_models."""
from views.view_user_entry import ViewUserEntry


class Match:
    """CLass Match."""

    def __init__(self, name, pairs_players):
        """Initialise un match."""
        self.name = name
        self.player_1 = pairs_players[0]
        self.player_2 = pairs_players[1]
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.winner = ""

    def __repr__(self):
        # Méthode __repr__ called
        return ([self.player_1, self.score_player_1],
                [self.player_2, self.score_player_2])

    def match_played(self):
        """Affiche le match qui est joué et affiche la sélection pour saisir le gagnant."""
        winner = ViewUserEntry().user_entry(
            message_display=f"{self.player_1.name} {self.player_1.surname} --VS-- " +
                            f"{self.player_2.name} {self.player_2.surname}\n"

                            f"Sélectionner le gagnant\n"
                            f"1 - {self.player_1.name} {self.player_1.surname}\n"
                            f"2 - {self.player_2.name} {self.player_2.surname}\n"
                            f"3 - Égalité\n> ",
            message_error="Sélectionner 1, 2 ou 3",
            value_type="Sélection",
            assertions=["1", "2", "3"]
        )
        print()

        if winner == "1":
            self.winner = self.player_1.name, self.player_1.surname
            self.score_player_1 += 1
        elif winner == "2":
            self.winner = self.player_2.name, self.player_2.surname
            self.score_player_2 += 1
        elif winner == "3":
            self.winner = "Égalité"
            self.score_player_1 += 0.5
            self.score_player_2 += 0.5

        self.player_1.tournament_score += self.score_player_1
        self.player_2.tournament_score += self.score_player_2

    def serialized_match(self):
        """Serialize les infos d'un match et renvoie ces informations."""
        match_infos = {}
        match_infos['player 1'] = self.player_1.serialized_player(save_tournament_score=True)
        match_infos['score player 1'] = self.score_player_1
        match_infos['player 2'] = self.player_2.serialized_player(save_tournament_score=True)
        match_infos['score player 2'] = self.score_player_2
        match_infos['winner'] = self.winner
        match_infos['name'] = self.name

        return match_infos
