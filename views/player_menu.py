from views.view_user_entry import ViewUserEntry


class CreatePlayer(ViewUserEntry):
    """Player view."""
    def display_create_player_menu(self):
        
        """Saisie pour le prénom"""
        name = input("Tapez le prénom du joueur : ")

        """Saisie pour le nom"""
        surname = input("Tapez le nom du joueur : ")

        """Saisie pour la date d'anniversaire"""
        #birthday_date_input = input("Tapez la date de naissance du joueur : ")
        birthday_date = self.user_entry(
            message_display="Tapez la date de naissance du joueur (format DD/MM/YYYY) :\n> ",
            message_error="Veuillez entrer une date au format valide : DD/MM/YYYY",
            value_type="date"
        )

        """Saisie du sexe"""
        sexe = self.user_entry(
            message_display="Sexe (H ou F) :\n ",
            message_error="Veuillez entrer H ou F",
            value_type="Sélection",
            assertions=["H", "h", "F", "f"]
        )

        """Saisie pour le classement"""
        #rank_input = input("Tapez le classement du joueur : ")
        rank = self.user_entry(
            message_display="Tapez le classement du joueur\n> ",
            message_error="Veuillez entrer une valeur numérique valide",
            value_type="numeric"
        )

        """Saisie du score"""
        total_score = self.user_entry(
            message_display="Entrer le score total\n> ",
            message_error="Veuillez entrer une valeur numérique valide",
            value_type="numeric"
        )

        """Saisie du score de tournoi"""
        tournament_score = self.user_entry(
            message_display="Entrer le score de tournoi\n> ",
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

    def display_loading_player(self, number_players_loading):

        all_players = loading_database("players")
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



def test_main():

    create_player = CreatePlayer()
    create_player.display_create_player_menu()


if __name__ == "__main__":
    test_main()
