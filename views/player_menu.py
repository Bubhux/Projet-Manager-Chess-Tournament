"""Module player_menu."""
from rich.console import Console
from rich.table import Table
from views.view_user_entry import ViewUserEntry
from controllers.database_controllers import DataBase

console = Console()


class CreatePlayer(ViewUserEntry):
    """Class création de joueurs."""
    def display_create_player_menu(self):
        """Fonction d'affichage du menu de création de joueur."""
        console.print("Tapez le prénom du joueur :", style="bold blue")
        name = input("> ")

        console.print("Tapez le nom du joueur :", style="bold blue")
        surname = input("> ")

        birthday_date = self.user_entry(
            message_display="Tapez la date de naissance du joueur (format DD/MM/YYYY) :\n> ",
            message_error="Veuillez entrer une date au format valide : DD/MM/YYYY",
            value_type="date"
        )

        """Saisie du sexe."""
        console.print("Sexe (H ou F) :", style="bold blue")
        sexe = self.user_entry(
            message_display=" ",
            message_error="Veuillez entrer H ou F",
            value_type="Sélection",
            assertions=["H", "h", "F", "f"]
        )

        """Saisie pour le classement."""
        console.print("Tapez le classement du joueur :", style="bold blue")
        rank = self.user_entry(
            message_display="> ",
            message_error="Veuillez entrer une valeur numérique valide",
            value_type="numeric"
        )

        console.print(f"Le joueur {name} {surname} est créé", style="bold green")

        return {
            "name": name,
            "surname": surname,
            "birthday_date": birthday_date,
            "sexe": sexe,
            "rank": rank,
            "total_score": 0,
            "tournament_score": 0,
        }


class LoadindPlayer(ViewUserEntry):
    """Class pour le chargement de joueur."""

    def display_loading_player(self, number_players_loading):
        """Affiche le menu pour le chargement d'un joueur."""
        database = DataBase()
        all_players = database.loading_database(database_name="players")
        serialized_loading_players = []

        for i in range(int(number_players_loading)):
            console.print(f"Plus que {str(int(number_players_loading) - i)} joueurs à charger", style="bold green")
            table = Table(title="Sélectionner un joueur", title_justify="left")
            table.add_column("ID", style="bold magenta")
            table.add_column("Nom", style="bold magenta")
            table.add_column("Prénom", style="bold magenta")

            assertions = []
            for i, player in enumerate(all_players):
                table.add_row(str(i+1), player['name'], player['surname'])
                assertions.append(str(i+1))

            console.print(table)

            user_input = int(self.user_entry(
                message_display="> ",
                message_error="Veuillez entrer un nombre entier",
                value_type=assertions
            ))
            if all_players[user_input-1] not in serialized_loading_players:
                serialized_loading_players.append(all_players[user_input-1])
            else:
                console.print("Ce joueur est déjà chargé sélectionner un autre joueur", style="bold red")
                number_players_loading += 1

        return serialized_loading_players
