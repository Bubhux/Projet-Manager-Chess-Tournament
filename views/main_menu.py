from views.view_user_entry import ViewUserEntry
from views.player_menu import CreatePlayer
from controllers.tournament_controllers import create_tournament


class MainMenu(ViewUserEntry):
    """Affiche le menu principal"""
    def display_main_menu(self):

        while True:
            print()
            user_input = self.user_entry(
                message_display="Sélectionner\n"
                                "0 - Créer un tournoi\n"
                                "1 - Créer des joueurs\n"
                                "2 - Charger un tournoi\n"
                                "3 - Voir les rapports\n"
                                "q - Quitter\n> ",
                message_error="Entrer une valeur valide",
                value_type="Sélection",
                assertions=["0", "1", "2", "3", "q"]
            )

            # Créer un tournoi
            if user_input == "0":
                tournament = create_tournament()
                break

            # Créer des joueurs
            elif user_input == "1":
                user_input = self.user_entry(
                    message_display="Nombre de joueurs à créer :\n> ",
                    message_error="Entrer une valeur numérique valide ",
                    value_type="numeric"
                )
                for i in range(user_input):
                    serialized_new_player = CreatePlayer().display_create_player_menu()
                    save_db("players", serialized_new_player)

            # Charger un tournoi
            elif user_input == "2":
                serialized_tournament = LoadTournament().display_menu()
                if serialized_tournament:
                    tournament = load_tournament(serialized_tournament)
                    break
                else:
                    print("Aucun tournoi sauvegardé !")
                    continue

            # Voir les rapports
            elif user_input == "3":
                while True:
                    user_input = self.user_entry(
                        message_display="0 - Joueurs\n1 - Tournois\nr - Retour\n> ",
                        message_error="Veuillez faire un choix valide.",
                        value_type="Sélection",
                        assertions=["0", "1", "r"]
                    )

                    if user_input == "r":
                        break

                    elif user_input == "0":
                        while True:
                            user_input = self.user_entry(
                                message_display="Voir le classement:\n"
                                                "0 - Par rang\n"
                                                "1 - Par ordre alphabétique\n"
                                                "r - Retour\n> ",
                                message_error="Veuillez faire un choix valide.",
                                value_type="Sélection",
                                assertions=["0", "1", "r"]
                            )
                            if user_input == "r":
                                break
                            elif user_input == "0":
                                sorted_players = Report().sort_players(Report().players, by_rank=True)
                                Report().display_players_report(players=sorted_players)
                            elif user_input == "1":
                                sorted_players = Report().sort_players(Report().players, by_rank=False)
                                Report().display_players_report(players=sorted_players)

                    elif user_input == "1":
                        Report().display_tournaments_reports()
            else:
                quit()

            """
            # Créer des joueurs
            elif user_input == "1":
                user_input = self.user_entry(
                    message_display = "Nombre de joueurs à créer:\n",
                    message_error = "Entrer une valeur numérique valide\n",
                    value_type = "numeric"
                )

            # Charger un tournoi 
            elif user_input == "2":
                if bdd_tournament:
                    tournament = loading_tournament()
                    break
                else:
                    print("Aucun tournoi sauvgardé !")
                    continue 
            """

def test_main():

    main_menu = MainMenu()
    main_menu.display_main_menu()


if __name__ == "__main__":
    test_main()
