"""Définit les classes propres à notre tournoi."""

NUMBER_PLAYER = 8


class Player:
    """Joueur."""

    def __init__(self, name, surname, birthday_date, sexe, total_score=None, tournament_score=None, rank=None):
        """Initialise le nom de famille, le prénom, la date de naissance, le sexe, le classement."""
        self.name = name
        self.surname = surname
        self.birthday_date = birthday_date
        self.sexe = sexe
        self.total_score = total_score
        self.tournament_score = tournament_score
        self.rank = rank
        self.played_with = []

    def __str__(self):
        return f"Joueur {self.name} {self.surname} {self.tournament_score} pts"
               #f"Le score de tournoi du joueur {self.name} {self.surname} est de : {self.tournament_score}"
               #f"{self.surname} {self.name}, classement : {self.rank}, {self.tournament_score} pts"


    #def __repr__(self):
        #return f"{self.surname} {self.name}, classement : {self.rank}, {self.tournament_score} pts"

    def __repr__(self):
        return str(self)

    def serialized_player(self, save_tournament_score=False):
        player_infos = {}
        player_infos['name'] = self.name
        player_infos['surname'] = self.surname
        player_infos['birthday date'] = self.birthday_date
        player_infos['sexe'] = self.sexe
        player_infos['total score'] = self.total_score
        player_infos['tournament score'] = self.tournament_score
        player_infos['rank'] = self.rank

        if save_tournament_score:
            player_infos['tournament_score'] = self.tournament_score

        return player_infos
