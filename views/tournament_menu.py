"""Module tournament_menu."""
from views.view_user_entry import ViewUserEntry
from controllers.database_controllers import DataBase


class CreateTournament(ViewUserEntry):
    """Class création tournoi menu interface."""

    def display_tournament_menu(self):
        """Affichage le menu de saisie lors de la création d'un tournoi."""
        view = ViewUserEntry()
        date = view.display_check_timestamp()
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
    """Class LoadingTournament."""

    def display_loading_tournament_menu(self):
        """Affiche le menu pour charger un tournoi."""
        database = DataBase()

        all_tournaments = database.loading_database("tournaments")
        if all_tournaments:

            builded_selection = self.build_selection(iterable=all_tournaments,
                                                     display_message="Sélectionner un tournoi :\n",
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
