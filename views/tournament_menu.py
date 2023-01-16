from views.view_user_entry import ViewUserEntry, display_check_timestamp
#from controllers.database_controllers import DataBase, loading_database
#from models.match_models import Match



class CreateTournament(ViewUserEntry):

    def display_tournament_menu(self):

        date = display_check_timestamp()
        print(date + " : Nouveau tournoi")

        name = input("Nom du tournoi :\n> ")
        description = input("Description du tournoi :\n> ")

        location = self.user_entry(
            message_display="Lieu :\n> ",
            message_error="Entrer un lieu valide",
            value_type="string"
        )

        user_selection_time = self.user_entry(
            message_display="Contrôle de temps :\n1 - Bullet\n2 - Blitz\n3 - Coup rapide\n> ",
            message_error="Veuillez entrer 1, 2 ou 3",
            value_type="Sélection",
            assertions=["1", "2", "3"]
        )

        if user_selection_time == "1":
            time_control = "Bullet"
        elif user_selection_time == "2":
            time_control = "Blitz"
        else:
            time_control = "Coup rapide"

        number_players = self.user_entry(
            message_display="Nombre de joueurs :\n> ",
            message_error="Veuillez entrer un nombre entier supérieur à 1 ou 2",
            value_type="numeric_superior",
            defaut_value=2
        )

        number_tours = self.user_entry(
            message_display="Nombre de tours (4 par défaut) :\n> ",
            message_error="Veuillez entrer 4 ou plus",
            value_type="numeric_superior",
            defaut_value=4
        )

        return {
            "name": name,
            "description": description,
            "location": location,
            "date": date,
            "time_control": time_control,
            "number_players": number_players,
            "number_tours": number_tours
        }

class LoadingTournament(ViewUserEntry):

    def display_loading_tournament_menu(self):

        all_tournaments = loading_database("tournaments")
        if all_tournaments:

            builded_selection = self.build_selection(iterable=all_tournaments,
                                                     dislay_message="Sélectionner un tournoi :\n",
                                                     assertions=[])

            user_input = int(self.user_entry(
                message_display=builded_selection['message'] + "\n> ",
                message_error="Sélectionner un nombre entier",
                value_type="Sélection",
                assertions=builded_selection['assertions']
            ))
            serialized_loading_tournament = all_tournaments[user_input - 1]

            return serialized_loading_tournament

        else:
            return False
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

def test_main():

     create_tournament = CreateTournament()
     create_tournament.display_tournament_menu()


if __name__ == "__main__":
    test_main()


