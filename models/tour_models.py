"""Module tour_models."""
from models.match_models import Match
from views.view_user_entry import ViewUserEntry


class Tour:
    """Class Tour."""

    def __init__(self, name, pairs_players, loading_match=False):
        """Initialise un tour."""
        view = ViewUserEntry()
        self.name = name
        self.pairs_players = pairs_players
        self.list_of_tours = []

        if loading_match:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()

        self.time_start = view.display_check_timestamp()
        self.time_end = ""

    def __str__(self):
        # Méthode __str__ called
        return self.name

    def create_matchs(self):
        """Création des matchs renvoie les matchs."""
        matchs = []
        for i, pair in enumerate(self.pairs_players):
            matchs.append(Match(name=f"Match {i}", pairs_players=pair))
        return matchs

    def match_completed(self):
        """Affiche un match terminé pour y saisir les résultats."""
        view = ViewUserEntry()
        self.date_end = view.display_check_timestamp()
        print(f"{self.date_end} : {self.name} terminé ")
        print("Rentrer les résultats des matchs : ")
        for match in self.matchs:
            match.match_played()

    def serialized_tour(self):
        """Serialize les infos d'un tour et les renvoies."""
        serialized_pairs_players = []
        for pair in self.pairs_players:
            serialized_pairs_players.append((
                    pair[0].serialized_player(save_tournament_score=True),
                    pair[1].serialized_player(save_tournament_score=True)
                ))

        return {
            "name": self.name,
            "pairs players": serialized_pairs_players,
            "matchs": [match.serialized_match() for match in self.matchs],
            "time start": self.time_start,
            "time end": self.time_end,
        }
