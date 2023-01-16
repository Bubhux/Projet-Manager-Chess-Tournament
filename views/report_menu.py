from views.view_user_entry import ViewUserEntry
#from controllers.database_controllers import DataBase, loading_database
from operator import itemgetter


class Report(ViewUserEntry):

    def __init__(self):
        self.players = loading_database("players")
        self.tournaments = loading_database("tournaments")

    def display_menu_players_report(self, players=[]):

        players = players

        builded_selection = self.build_selection(iterable=players,
                                                 display_message="Voir les détails d'un joueur:\n",
                                                 assertions=["r"])

        while True:
            print("Classement: ")

            # Affichage du classement
            # Choix d'un joueur dans le classement afin de voir ses détails
            user_input = self.user_entry(
                message_display=builded_selection['message'] + "r - Retour\n> ",
                message_error="Veuillez faire un choix valide.",
                value_type="Sélection",
                assertions=builded_selection['assertions']
            )

            if user_input == "r":
                break

            else:
                selected_player = players[int(user_input) - 1]

                # Affichage des détails du joueur
                while True:
                    print(f"Détails du joueur {selected_player['name']}:")
                    print(f"Rang: {selected_player['rank']}\n"
                          f"Score total: {selected_player['total_score']}\n"
                          f"Nom: {selected_player['name']}\n"
                          f"Prénom: {selected_player['surname']}\n"
                          f"Date de naissance: {selected_player['birthday_date']}\n"
                          f"Sexe: {selected_player['sexe']}\n"
                          )

                    user_input = self.user_entry(
                        message_display="Sélectionner\n r - Retour\n> ",
                        message_error="Veuillez faire un choix valide.",
                        value_type="selection",
                        assertions=["r"]
                    )
                    if user_input == "r":
                        break

    def display_menu_tournaments_reports(self):

        builded_selection = self.build_selection(
            iterable=self.tournaments,
            display_message="Voir les détails d'un tournoi:\n",
            assertions=['r']
        )

        while True:
            print("Tournois:")

            # Affichage de tout les tournois
            # Choix d'un tournoi afin d'en voir les détails

            user_input = self.user_entry(
                message_display=builded_selection['message'] + "r - Retour\n> ",
                message_error="Veuillez faire un choix valide.",
                value_type="Sélection",
                assertions=builded_selection['assertions']
            )

            if user_input == "r":
                break

            else:
                selected_tournament = self.tournaments[int(user_input) - 1]

                # Affichage des détails du tournoi choisi

                while True:
                    print(f"Détails du tournoi {selected_tournament['name']}\n"
                          f"Nom: {selected_tournament['name']}\n"
                          f"Lieu: {selected_tournament['location']}\n"
                          f"Date: {selected_tournament['date']}\n"
                          f"Contrôle du temps: {selected_tournament['time_control']}\n"
                          f"Nombre de tours: {selected_tournament['number_tours']}\n"
                          f"Description: {selected_tournament['description']}\n"
                          )

                    user_input = self.user_entry(
                        message_display="Sélectionner\n"
                                    "1 - Voir les participants\n"
                                    "2 - Voir les tours\n"
                                    "r - Retour\n"
                                    "> ",
                        message_error="Veuillez entrer une sélection valide",
                        value_type="Sélection",
                        assertions=["1", "2", "3", "r"]
                    )

                    if user_input == "r":
                        break

                    elif user_input == "1":
                        while True:
                            user_input = self.user_entry(
                                message_display="Type de classement:\n"
                                            "1 - Par rang\n"
                                            "2 - Par ordre alphabétique\n"
                                            "r - Retour\n"
                                            "> ",
                                message_error="Veuillez entrer une sélection valide",
                                value_type="Sélection",
                                assertions=["1", "2", "r"]
                            )

                            if user_input == "r":
                                break
                            elif user_input == "1":
                                sorted_players = self.sort_players(selected_tournament["players"], by_rank=True)
                                self.display_menu_players_report(players=sorted_players)
                            elif user_input == "2":
                                sorted_players = self.sort_players(selected_tournament["players"], by_rank=False)
                                self.display_menu_players_report(players=sorted_players)
                    elif user_input == "1":
                        self.display_menu_rounds(selected_tournament["tours"])

    def display_menu_tours(self, tours: list):
        builded_selection = self.build_selection(
            iterable=tours,
            display_message="Voir les détails d'un tour:\n",
            assertions=['r']
        )
        while True:
            print("Tours:")

            user_input = self.user_entry(
                message_display=builded_selection['message'] + "r - Retour\n> ",
                message_error="Veuillez faire un choix valide.",
                value_type="Sélection",
                assertions=builded_selection['assertions']
            )

            if user_input == "r":
                break

            else:
                selected_tour = tours[int(user_input) - 1]
                while True:
                    print(f"Détails du tour {selected_tour['name']}\n"
                          f"Nom: {selected_tour['name']}\n"
                          f"Nombre de matchs: {len(selected_tour['matchs'])}\n"
                          f"Date de début: {selected_tour['time_start']}\n"
                          f"Date de fin: {selected_tour['time_end']}\n"
                          )
                    user_input = self.user_entry(
                        message_display="Sélectionner\n1 - Voir les matchs\nr - Retour\n> ",
                        message_error="Veuillez faire un choix valide",
                        value_type="Sélection",
                        assertions=["1", "r"]
                    )
                    if user_input == "r":
                        break
                    else:
                        builded_selection = self.build_selection(
                            iterable=selected_round['matchs'],
                            display_message="Voir les détails d'un match\n",
                            assertions=['r']
                        )
                        print("Matchs:")
                        user_input = self.user_entry(
                            message_display=builded_selection['message'] + "r - Retour\n> ",
                            message_error="Veuillez faire un choix valide.",
                            value_type="Sélection",
                            assertions=builded_selection['assertions']
                        )

                        if user_input == "r":
                            break
                        else:
                            selected_match = selected_round['matchs'][int(user_input) - 1]
                            while True:
                                print(f"Détails du {selected_match['name']}\n"
                                      #f"Joueur 1 ({selected_match['color_player1']}): " +
                                      f"{selected_match['player1']['name']} ({selected_match['score_player1']} pts)\n"
                                      #f"Joueur 2 ({selected_match['color_player2']}): " +
                                      f"{selected_match['player2']['name']} ({selected_match['score_player2']} pts)\n"
                                      f"Gagnant: {selected_match['winner']}\n"
                                      )
                                user_input = self.user_entry(
                                    message_display="Sélectionner\nr - Retour\n> ",
                                    message_error="Veuillez faire un choix valide",
                                    value_type="selection",
                                    assertions=["r"]
                                )
                                if user_input == "r":
                                    break

    @staticmethod
    def sort_players(players: list, by_rank: bool) -> list:

        if by_rank:
            sorted_players = sorted(players, key=itemgetter('rank'))
        else:
            sorted_players = sorted(players, key=itemgetter('name'))

        return sorted_players


		