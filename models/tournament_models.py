"""Définit le tournoi."""
from models.tour_models import Tour


class Tournament:
    """Tournoi"""

    def __init__(self, name, location, date, time_control, players, description=None, number_tours=4):
                """Initialise initialise le tournoi"""
                self.name = name
                self.location = location
                self.date = date
                self.time_control = time_control
                self.players = players
                self.description = description
                self.number_tours = number_tours
                self.tours = []

    def __str__(self):
        return f"Tournoi: {self.name} {self.description} à {self.location}"

    def __repr__(self):
        return f"Tournoi: {self.name} {self.description} à {self.location}"

    def create_tour(self, tour_number):
        pairs_players = self.create_pairs_players(current_tour=tour_number)
        tour = Tour("Tour " + str(tour_number + 1), pairs_players)
        self.tours.append(tour)

    def create_pairs_players(self, current_tour):
        """Création des paires de joueurs"""

        # Trie les joueurs par rapport à leurs classement pour le premier tour
        if current_tour == 0:
            sorted_players = sorted(self.players, key=lambda x: x.rank)
            print("---test current_tour 1---")

        # Trie les joueurs par rapport à leurs scrore total pour le tour suivant
        #elif current_tour == 3 or current_tour == 7:
        #if current_tour > 0:
        else:
            sorted_players = []
            #print(f"liste sorted_players {(sorted_players)}")
            score_sorted_players = sorted(self.players, key=lambda x: x.tournament_score)
            print("---test next_current_tour---")

            # Si deux joueurs ont le même score on les trie par rapport à leurs rangs
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

        # Trie les joueurs en 2 parties
        sup_player_part = sorted_players[len(sorted_players)//2:]
        inf_player_part = sorted_players[:len(sorted_players)//2]

        print(f"liste sup_player_part {(sup_player_part)}")
        print(f"liste inf_player_part {(inf_player_part)}")
        print(f"liste sorted_players {(sorted_players)}")

        """
        pairs_players = []

        # Création des paires de joueurs
        for i, player in enumerate(sup_player_part):
            played_with = []
            z = 0
            while True:
                try:
                    player_2 = inf_player_part[i+z]

                except IndexError:
                    # Asssignation du dernier joueur de la partie supérieur au dernier joueur de la partie inférieur
                    player_2 = inf_player_part[i]
                    pairs_players.append((player, player_2))

                    # Assignation des joueurs dans la liste "played_with" pour indiquer qu'ils ont déja jouer ensemble
                    player_2.played_with.append(player)
                    player.played_with.append(player_2)
                    break

                # Si player a joué contre player_2, on test avec player_3
                if player in player_2.played_with:
                    z += 1
                    continue

                # Si les 2 players n'ont jamais joués ensemble on crée la paires
                # Sinon on assigne les players dans la liste played_with pour indiquer qu'ils ont déja joués ensemble
                else:
                    pairs_players.append((player, player_2))
                    player_2.played_with.append(player)
                    player.played_with.append(player_2)
                    break

        return pairs_players
        """
        pairs_players = []

        # Création des paires de joueurs
        #count_player = 0

        for i, player in enumerate(sup_player_part):
            count_player = 0
            #played_with = []
            #list_pairs_players = True
            #played_with = True
            #indice_inf_player_part = len(inf_player_part)-1
            player_2 = inf_player_part[i+count_player]

            # Asssignation du premier joueur de la partie supérieur au premier joueur de la partie inférieur
            #player_2 = inf_player_part[indice_inf_player_part-i]
            #player_2 = inf_player_part[i]
            pairs_players.append((player, player_2))
            print(f"Liste pairs_players {(pairs_players)}")

            # Assignation des joueurs dans la liste "played_with" pour indiquer qu'ils ont déja jouer ensemble
            player.played_with.append(player_2) 
            player_2.played_with.append(player) 
            print(f"Liste played_with {(player.played_with)}")
            print(f"Liste played_with {(player_2.played_with)}")
            #break
            #continue

            # si le joueur 1 à déja jouer contre le joueur 2 passer à joueur 3
            #if current_tour > 0 and player in played_with:
            #if current_tour != 3 and !=7:
            if player in player_2.played_with:
                #for player in played_with:
                count_player += 1
                print("---test count_player---")
                #continue # la boucle continue même si la condition est déclenchée

            # Si les 2 joueurs n'ont jamais joués ensemble on crée la paire
            # Sinon on assigne les joueurs dans la liste played_with pour indiquer qu'ils ont déja joués ensemble
            else:
                pairs_players.append((player, player_2)) 
                played_with.append(player)
                played_with.append(player_2)
                #continue
                #break

        return pairs_players
        
    def tournament_rankings(self, score_ranking=True):

        # Renvoie le classement du tournoi par rapport aux points de chaque joueurs
        if score_ranking:
            sorted_players = sorted(self.players, key=lambda x: x.tournament_score)
        else:
            sorted_players =sorted(self.players, key=lambda x: x.rank)

        return sorted_players

    def serialized_tournament(self, save_tours=False):
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



"""
pairs_players = []
liste_player = ["player_1", "player_2", "player_3", "player_4"]

tour 1 : match 1 => player_1 vs player_3, match 2 => player_2 vs player_4

tour 2 : match 1 => player_1 vs player_4, match 2 => player_2 vs player_3
for player in list_player[::3]:
    print(player)
    pairs_players.append(player)
    print(pairs_players)

return pairs_players

player_1
player_4
["player_1", "player_4"]

for player in list_player[1:3]:
    print(player)
    pairs_players.append(player)
    print(pairs_players)

return pairs_players

player_2
player_3
["player_2", "player_3"]

tour 3 : match 1 => player_1 vs player_2, match 2 => player_3 vs player_4
for player in list_player[0:2]:
    print(player)
    pairs_players.append(player)
    print(pairs_players)

return pairs_players

player_1
player_2
["player_1", "player_2"]

for player in list_player[2:5]:
    print(player)
    pairs_players.append(player)
    print(pairs_players)

return pairs_players

player_3
player_4
[player_3", "player_4"]

tour 4 : trie par le score si les scrores du tournoi sont égaux trie par le rank 
"""












