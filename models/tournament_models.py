"""Module tournament_models."""
from models.tour_models import Tour
from itertools import permutations
from random import shuffle


class Tournament:
    """Class Tournoi."""

    def __init__(self, name, location, date, time_control, players, description="", number_tours=4):
        """Initialise un tournoi."""
        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.players = players
        self.description = description
        self.number_tours = number_tours
        self.tours = []
        self.match_played = []

    def __str__(self):
        """Méthode __str__ called."""
        return f"Tournoi: {self.name} {self.description} à {self.location}"

    def __repr__(self):
        """Méthode __repr__ called."""
        return str(self)

    def create_tour(self, tour_number):
        """Fonction qui creé un tour."""
        pairs_players = self.create_pairs_players(current_tour=tour_number)
        tour = Tour("Tour " + str(tour_number + 1), pairs_players)
        self.tours.append(tour)

    def create_pairs_players(self, current_tour):
        """Création des paires de joueurs."""
        pairs_players = []
        sorted_players = []
        list_score_sorted_players = []

        # Premier tour l'appariement des joueurs et fait par le classement.
        if current_tour == 0:
            sorted_players = sorted(self.players, key=lambda x: x.rank, reverse=True)

            sup_player_part = sorted_players[len(sorted_players)//2:]
            inf_player_part = sorted_players[:len(sorted_players)//2]

            # Création des paires de joueurs pour le premeir tour.
            for i, player in enumerate(sup_player_part):
                count_player = 0
                player_2 = inf_player_part[i+count_player]

                # Asssignation du premier joueur de la partie supérieur au premier joueur de la partie inférieur.
                pairs_players.append((player, player_2))
                self.match_played.append((player, player_2))

                player.played_with.append(player_2)
                player_2.played_with.append(player)

                if player in player_2.played_with:
                    count_player += 1

                else:
                    pairs_players.append((player, player_2))
                    player_2.played_with.append(player)
                    player.played_with.append(player_2)

        # Pour les tours compris entre le premier et le dernier tour.
        # L'appariement des joueurs est fait de facon aléatoire et non répetitives.
        # Chaque joueur fait le même nombre de matchs.
        elif current_tour < self.number_tours - 1:
            sorted_players = sorted(self.players)
            pairs = list(permutations(sorted_players, 2))  # permutations de longueur 2 
            shuffle(pairs)                                 # mélanger 

            for x in pairs:
                pairs_players.append(x)

            # Chaque élément pair va remplir la liste si.
            # L'élément pair trié n’existe pas déjà dans la liste pairs_players.
            # Exemple élément pair = (1, 2) donnant (2, 1) sera rejeté puisque il existe déjà.
            # Ou si l'élément trié est égal à lui même avant d'être trié.
            # Exemple l'élément pair = (1, 2), donnant (1, 2) sera conservé puisque il est égal à lui-même.
            pairs_players = [
                x for x in pairs
                if tuple(sorted(x))
                not in pairs
                or tuple(sorted(x)) == x
            ]

            for x in tuple(sorted(self.match_played)):
                try:
                    pairs_players.remove(x)
                except ValueError:
                    pass

            exclude_indice_players = set()
            match_list_available = []

            # Exclue les indices de 2 joueurs sur les paires génerées de maniére aléatoires.
            # Pour que lors d'un tour un joueur ne joue pas 2 matchs.
            for x in pairs_players:
                if (x[0] not in exclude_indice_players and x[1] not in exclude_indice_players):
                    match_list_available.append(x)
                    exclude_indice_players.add(x[0])
                    exclude_indice_players.add(x[1])

                    for player in exclude_indice_players:
                        exclude_indice_players.add(player)

            pairs_players = match_list_available

            if len(self.players) == 8:
                pairs_players = pairs_players[:4]
            else:
                pairs_players = pairs_players[:2]

        # Pour le dernier tour l'appariement des joueurs est fait par le score ou le classement.
        # Si deux joueurs ont le même score on les trie par rapport à leurs rangs.
        # De cette maniére les joueurs ayant le même niveau s'affronte.
        else:
            score_sorted_players = sorted(self.players, key=lambda x: x.tournament_score, reverse=True)
            for i, player in enumerate(score_sorted_players):
                try:
                    sorted_players.append(player)
                except player.tournament_score == score_sorted_players[i+1].tournament_score:
                    if player.rank > score_sorted_players[i+1].rank:
                        sup_player = player
                        inf_player = score_sorted_players[i+1]
                    else:
                        sup_player = score_sorted_players[i+1]
                        inf_player = player
                        sorted_players.append(sup_player)
                        sorted_players.append(inf_player)
                except IndexError:
                    sorted_players.append(player)

            if len(self.players) == 8:
                list_score_sorted_players = (sorted_players[:2], sorted_players[2:4],
                                             sorted_players[4:6], sorted_players[6:])

            else:
                list_score_sorted_players = sorted_players[:2], sorted_players[2:]

            pairs_players = [tuple(x) for x in list_score_sorted_players]

        return pairs_players

    def tournament_rankings(self, score_ranking=True):
        """Renvoie le classement du tournoi par rapport aux points de chaque joueurs."""
        if score_ranking:
            sorted_players = sorted(self.players, key=lambda x: x.tournament_score, reverse=True)
        else:
            sorted_players = sorted(self.players, key=lambda x: x.rank, reverse=True)

        return sorted_players

    def serialized_tournament(self, save_tours=False):
        """Serialize les infos tournois et renvoie ces informations."""
        tournament_infos = {}
        tournament_infos['name'] = self.name
        tournament_infos['location'] = self.location
        tournament_infos['date'] = self.date
        tournament_infos['time control'] = self.time_control
        tournament_infos['players'] = [player.serialized_player(save_tournament_score=True) for player in self.players]
        tournament_infos['description'] = self.description
        tournament_infos['number tours'] = self.number_tours
        tournament_infos['tours'] = [tour.serialized_tour() for tour in self.tours]

        if save_tours:
            tournament_infos['tours'] = [tour.serialized_tour() for tour in self.tours]

        return tournament_infos
