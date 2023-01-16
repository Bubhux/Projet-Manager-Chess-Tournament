"""Définie les tours."""
import time
from models.match_models import Match
#from views.tournament_menu import DisplayTour
from views.view_user_entry import ViewUserEntry, display_check_timestamp
from views.view_user_entry import DisplayTour


#NUMBER_TOURS = 4

class Tour:
    """Tour"""

    #MATCH_NUMBER = 1

    def __init__(self, name, pairs_players, loading_match=False):
        """Initialise le nom, le début du tour, la fin du tour, la liste des matchs finis"""
        self.name = name
        #self.time_start = time_start
        #self.time_end = time_end
        self.pairs_players = pairs_players
        #self.list_matchs_finished = list_matchs_finished
        self.list_of_tours = []

        if loading_match:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()

        self.time_start = display_check_timestamp()
        self.time_end = ""
    
    def __str__(self):
        return self.name
        
    """
    def __str__(self):
        return f"{self.name} Début : {self.time_start} Fin : {self.time_end}"

    def __repr__(self):
        return f"{self.name} Début : {self.time_start} Fin : {self.time_end}"
    """

    """
    def create_tours(self, tour_number):
        pairs_players = self.create_pairs_players(current_tour=tour_number)
        round = Tour("Tour" + str(tour_number + 1), pairs_players)
        self.tours.append(round)
    """
    def create_matchs(self):
        matchs = []
        for i, pair in enumerate(self.pairs_players):
            matchs.append(Match(name=f"Match {i}", pairs_players=pair))
        return matchs

    def match_completed(self):
        self.date_end = display_check_timestamp()
        print(f"{self.date_end} : {self.name} terminé ")
        print("Rentrer les résultats des matchs : ")
        for match in self.matchs:
            match.match_played()

    def serialized_tour(self):
        serialized_pairs_players = []
        for pair in self.pairs_players:
            serialized_pairs_players.append(
                (
                    pair[0].serialized_player(save_tournament_score=True),
                    pair[1].serialized_player(save_tournament_score=True)
                )

            )

        return {
            "name": self.name,
            "pairs_players": serialized_pairs_players,
            "matchs": [match.serialized_match() for match in self.matchs],
            "time_start": self.time_start,
            "time_end": self.time_end,
        }


    def run_tours(self, sorted_players_list, tournament_object):
        self.view = DisplayTour()
        self.list_of_tours = []
        self.list_matchs_finished = []
        self.name = "Tour" + str(len(tournament_object.list_of_tours) + 1)

        self.time_start, self.time_end = self.display_tour_time()

        # Ajoute des instances de "match" dans la liste "list_of_tours" tant qu'il y a des joueurs dans la liste
        while len(sorted_players_list) > 0:
            instance_match = Match(self.name, sorted_players_list[0], sorted_players_list[1])
            Match.MATCH_NUMBER += 1
            self.list_of_tours.append(instance_match)
            del sorted_players_list[:2]

        for match in self.list_of_tours:

            confirmed_score_player_1 = False
            while not confirmed_score_player_1:
            	score_player_1 = input(f"Entrez le score de {match.player_1} : ")
            	float(score_player_1)
            else:
            	match.score_player_1 = True

            confirmed_score_player_2 = False
            while not confirmed_score_player_2:
            	score_player_2 = enput(f"Entrez le score de {match.player_2} : ")
            	float(score_player_2)
            else:
            	match.score_player_2 = True

            self.list_matchs_finished.append(([match.player_1, match.score_player_1],
            	                              [match.player_2, match.score_player_2]))

        return Tour(self.name, self.time_start, self.time_end, self.list_matchs_finished)

"""
class DisplayTour:

    def __init__(self):
        self.match = match_models.Match()

    def display_tour(self, tour_name, list_matchs):

        print(f"---------------------{tour_name}---------------------\n")
        print()
        for match in list_matchs:
            print(match)
            print()

    def display_tour_time(self):
        print()
        input("Appuyez sur une touche pour commencer le tour")
        print()
        time_start = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f"Début du tour : {time_start}")
        print()
        input("Appuyez sur une touche lorsque le tour est terminé")
        time_end = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f"Fin du tour : {time_end}")
        print()
        return time_start, time_end
"""






