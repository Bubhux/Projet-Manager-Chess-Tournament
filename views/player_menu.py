"""Module player_menu."""
from views.view_user_entry import ViewUserEntry
from controllers.database_controllers import DataBase


class CreatePlayer(ViewUserEntry):
    """Class crétion de joueurs."""
    def display_create_player_menu(self):
        """Fonction d'affichage du menu de création de joueur."""
        name = input("Tapez le prénom du joueur : ")
        surname = input("Tapez le nom du joueur : ")

        birthday_date = self.user_entry(
            message_display="Tapez la date de naissance du joueur (format DD/MM/YYYY) :\n> ",
            message_error="Veuillez entrer une date au format valide : DD/MM/YYYY",
            value_type="date"
        )

        """Saisie du sexe."""
        sexe = self.user_entry(
            message_display="Sexe (H ou F) :\n ",
            message_error="Veuillez entrer H ou F",
            value_type="Sélection",
            assertions=["H", "h", "F", "f"]
        )

        """Saisie pour le classement."""
        rank = self.user_entry(
            message_display="Tapez le classement du joueur\n> ",
            message_error="Veuillez entrer une valeur numérique valide",
            value_type="numeric"
        )

        print(f"Le joueur {name} {surname} est créé")

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
        database = DataBase
        all_players = database.loading_database("players")
        serialized_loading_players = []
        for i in range(number_players_loading):
            print(f"Plus que {str(number_players_loading - i)} joueurs à charger")
            display_message = "Sélectionner un joueur:\n"

            assertions = []
            for i, player in enumerate(all_players):
                display_message = display_message + f"{str(i+1)} - {player['name']} {player['surname']}\n"
                assertions.append(str(i+1))

            user_input = int(self.user_entry(
                message_display=display_message,
                message_error="Veuillez entrer un nombre entier",
                value_type=assertions
            ))
            if all_players[user_input-1] not in serialized_loading_players:
                serialized_loading_players.append(all_players[user_input-1])
            else:
                print("Ce joueur est déjà chargé sélectionner un autre joueur")
                number_players_loading += 1

        return serialized_loading_players
