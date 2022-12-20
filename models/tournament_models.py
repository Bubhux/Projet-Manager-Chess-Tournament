"""Définit le tournoi."""




class Tournament:
    """Tournoi ."""
    def __init__(self, tournament_name=None,
                 location=None,
                 tournament_date=None,
                 time_control=None,
                 players=None,
                 description=None,
                 list_of_tours=[],
                 tournament=None,
                 played_with=[],
                 number_tours=4
                 ):
                """Initialise initialise le nom du tournoi, le lieu, la date."""

                self.tournament_name = tournament_name
                self.location = location
                self.tournament_date = tournament_date
                self.time_control = time_control
                self.players = players
                self.description = description
                self.list_of_tours = list_of_tours
                self.tournament = tournament
                self.played_with = played_with
                self.number_tours = number_tours

    def __str__(self):
        return f"{self.tournament_name} {self.location} {self.list_of_tours}"

    def __repr__(self):
        return f"{self.tournament_name} {self.location} {self.list_of_tours}"

    def create_pairs_players(self, current_tour):
        """Création des pairs de joueurs."""

        # Trie les joueurs par rapport à leurs classement pour le premier tour
        if current_tour == 0:
            rank_sorted_players = sorted(self.players, key=lambda x: x.rank)

        # Trie les joueurs par rapport à leurs scrore total pour le tour suivant
        else:
            sorted_players = []
            score_sorted_players = sorted(self.players, key=lambda x: x.total_score)

            # Si deux joueurs ont le même score, on les trie par rapport à leurs rangs
            for i, player in enumerate(score_sorted_players):
                sorted_players.append(player)

                if player.rank > score_sorted_players[i+1].rank:
                    sup.player = player
                    inf_player = score_sorted_players[i+1]
                else:
                    inf.player = player
                    sup.player = score_sorted_players[i+1]
                sorted_players.append(sup.player)
                sorted_players.append(inf_player)

        # Trie les joueurs en 2 parties 
        sup_player_part = sorted_players[:4]
        inf_player_part = sorted_players[4:]

        pairs_players = []

        # Création des pairs de joueurs 
        for i, player in enumerate(sup_player_part):
            z = 0 
            while True:
                player_2 = inf_player_part[i+z]

            # Asssignation du dernier joueur de la partie supérieur au dernier joueur de la partie inférieur
            player_2 = inf_player_part[i]
            pairs_players.append((player, player_2))

            # Assignation des joueurs dans la liste "played_with" pour indiquer qu'ils ont déja jouer ensemble
            played_with.append(player)
            played_with.append(player_2)
            break

            # Si player a joué contre player_2, on test avec player_3
            if player in player_2.played_with:
                z += 1 
                continue 

            # Si les 2 players n'ont jamais joués ensemble on crée la pairs
            # Sinon on assigne les players dans la liste plyed_with pour indiquer qu'ils ont déja joués ensemble
            else:
                pairs_players.append((player, player_2))
                played_with.append(player)
                played_with.append(player_2)
                break

        return pairs_players

    def get_ranking(self, score_ranking=True):

        # Renvoie le classement du tournoi par rapport aux points de chaque joueurs
        if score_ranking:
            sorted_players = sorted(self.players, key=lambda x: x.tournament_score)
        else:
            sorted_players =sorted(self.players, key=lambda x: x.rank)

        return sorted_players
        















