"""Module tournament_menu."""
from rich.console import Console

from views.view_user_entry import ViewUserEntry
from controllers.database_controllers import DataBase


class CreateTournament(ViewUserEntry):
    """Class création tournoi menu interface."""

    def display_tournament_menu(self):
        """Affichage le menu de saisie lors de la création d'un tournoi."""
        console = Console()
        view = ViewUserEntry()
        date = view.display_check_timestamp()
        console.print(date + " : Nouveau tournoi")

        console.print("Nom du tournoi :", style="bold blue")
        name = input("> ")

        console.print("Description du tournoi :", style="bold blue")
        description = input("> ")

        console.print("Lieu :", style="bold blue")
        location = self.user_entry(
            message_display="> ",
            message_error="Entrer un lieu valide",
            value_type="string"
        )

        console.print("Contrôle de temps :", style="bold blue")
        user_selection_time = self.user_entry(
            message_display="1 - Bullet\n2 - Blitz\n3 - Coup rapide\n> ",
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

        console.print("Nombre de joueurs :", style="bold blue")
        number_players = self.user_entry(
            message_display="> ",
            message_error="Veuillez entrer un nombre entier supérieur à 1 ou 2",
            value_type="numeric_superior",
            default_value=2
        )

        console.print("Nombre de tours (4 par défaut) :", style="bold blue")
        number_tours = self.user_entry(
            message_display="> ",
            message_error="Veuillez entrer 4 ou plus",
            value_type="numeric_superior",
            default_value=4
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
        console = Console()
        database = DataBase()

        all_tournaments = database.loading_database("tournaments")
        if all_tournaments:
            builded_selection = self.build_selection(
                iterable=all_tournaments,
                display_message="Sélectionner un tournoi :\n",
                assertions=["r"]  # Ajout de la touche 'r' pour retour
            )

            console.print(builded_selection['message'] + "r - Retour", style="bold blue")
            user_input = self.user_entry(
                message_display="> ",
                message_error="Sélectionner un nombre entier",
                value_type="Sélection",
                assertions=builded_selection['assertions']
            )

            if user_input == "r":
                return False  # Si l'utilisateur choisit de revenir, retourne False

            user_input = int(user_input)
            serialized_loading_tournament = all_tournaments[user_input - 1]

            return serialized_loading_tournament

        else:
            return False
