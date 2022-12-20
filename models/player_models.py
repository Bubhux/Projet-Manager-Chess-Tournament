"""Définit les classes propres à notre tournoi."""

NUMBER_PLAYER = 8


class Player:
    """Joueur."""

    def __init__(self, surname, name, date_of_birth, sexe, total_score, tournament_score, rank=0):
        """Initialise le nom de famille, le prénom, la date de naissance, le sexe, le classement."""
        self.surname = surname
        self.name = name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.total_score = total_score
        self.tournament_score = 0
        self.rank = rank

    def __str__(self):
    	return f"{self.surname} {self.name}, classement : {self.rank}, {self.tournament_score} pts"

    def __repr__(self):
    	return f"{self.surname} {self.name}, classement : {self.rank}, {self.tournament_score} pts"