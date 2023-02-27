"""Module player_models."""


class Player:
    """Class Player."""

    def __init__(self, name, surname, birthday_date, sexe, rank, total_score):
        """Initialise un joueur."""
        self.name = name
        self.surname = surname
        self.birthday_date = birthday_date
        self.sexe = sexe
        self.rank = rank
        self.total_score = total_score
        self.tournament_score = 0
        self.played_with = []

    def __lt__(self, other):
        # Méthode __lt__ called
        return (
                self.rank < other.rank
        )

    def __gt__(self, other):
        # Méthode __gt__ called
        return (
                self.rank > other.rank
        )

    def __eq__(self, other):
        # Méthode __eq__ called
        return (
                self.total_score == other.total_score
                and self.rank == other.rank
        )

    def __hash__(self):
        # Méthode __hash__ called
        return hash((
            self.name,
            self.surname,
            self.birthday_date,
            self.sexe,
            self.rank,
            self.total_score,
            self.tournament_score
        ))

    def __str__(self):
        # Méthode __str__ called
        return f"{self.name} {self.surname}, score tournoi {self.tournament_score} pts"

    def __repr__(self):
        # Méthode __repr__ called
        return str(self)

    def serialized_player(self, save_tournament_score=False):
        """Serialize les infos player et le renvoies."""
        player_infos = {}
        player_infos['name'] = self.name
        player_infos['surname'] = self.surname
        player_infos['birthday date'] = self.birthday_date
        player_infos['sexe'] = self.sexe
        player_infos['rank'] = self.rank
        player_infos['total score'] = self.total_score
        player_infos['tournament score'] = self.tournament_score

        if save_tournament_score:
            player_infos['tournament score'] = self.tournament_score

        return player_infos
