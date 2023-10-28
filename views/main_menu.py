"""Module main_menu."""
from views.view_user_entry import ViewUserEntry
from views.player_menu import CreatePlayer
from views.tournament_menu import LoadingTournament
from views.report_menu import Report

from controllers.tournament_controllers import create_tournament, play_tournament
from controllers.player_controllers import update_rankings
from controllers.database_controllers import DataBase


class MainMenu(ViewUserEntry):
    """Class affichage menu principal."""
    def display_main_menu(self):
        """Fonction affichage du menu principal."""
        database = DataBase()
        while True:
            print()
            user_input = self.user_entry(
                message_display="Sélectionner\n"
                                "1 - Créer un tournoi\n"
                                "2 - Créer des joueurs\n"
                                "3 - Charger un tournoi\n"
                                "4 - Voir les rapports\n"
                                "q - Quitter\n> ",
                message_error="Entrer une valeur valide",
                value_type="Sélection",
                assertions=["1", "2", "3", "4", "q"]
            )
            print()

            # Créer un tournoi.
            if user_input == "1":
                tournament = create_tournament()
                break

            # Créer des joueurs.
            elif user_input == "2":
                user_input = self.user_entry(
                    message_display="Nombre de joueurs à créer :\n> ",
                    message_error="Entrer une valeur numérique valide ",
                    value_type="numeric"
                )
                for i in range(user_input):
                    CreatePlayer().display_create_player_menu()
                    serialized_new_player = CreatePlayer().display_create_player_menu()
                    database.save_database("players", serialized_new_player)

            # Charger un tournoi.
            elif user_input == "3":
                serialized_tournament = LoadingTournament().display_loading_tournament_menu()
                if serialized_tournament:
                    tournament = database.loading_tournament(serialized_tournament)
                    break
                else:
                    print("Aucun tournoi sauvegardé. 1a")
                    continue
            # Voir les rapports.
            elif user_input == "4":
                while True:
                    user_input = self.user_entry(
                        message_display="1 - Joueurs\n2 - Tournois\nr - Retour\n> ",
                        message_error="Veuillez faire un choix valide.",
                        value_type="Sélection",
                        assertions=["1", "2", "r"]
                    )
                    print()

                    if user_input == "r":
                        break

                    elif user_input == "1":
                        while True:
                            user_input = self.user_entry(
                                message_display="Voir le classement:\n"
                                                "1 - Par rang\n"
                                                "2 - Par ordre alphabétique\n"
                                                "r - Retour\n> ",
                                message_error="Veuillez faire un choix valide.",
                                value_type="Sélection",
                                assertions=["1", "2", "r"]
                            )
                            print()
                            try:
                                if user_input == "r":
                                    break
                                elif user_input == "1":
                                    sorted_players = Report().sort_players(Report().players, by_rank=True)
                                    Report().display_menu_players_reports(players=sorted_players)

                                elif user_input == "2":
                                    sorted_players = Report().sort_players(Report().players, by_rank=False)
                                    Report().display_menu_players_reports(players=sorted_players)
                            except TypeError:
                                pass
                                print("Aucun joueurs sauvegardés.")
                                print()

                    elif user_input == "2":
                        try:
                            Report().display_menu_tournaments_reports()
                        except TypeError:
                            pass
                            print("Aucun tournoi sauvegardé.")
                            print()
            else:
                quit()

        # Lancement du tournoi.
        print()
        user_input = self.user_entry(
            message_display="Sélectionner\n"
                            "1 - Jouer le tournoi\n"
                            "q - Quitter\n> ",
            message_error="Veuillez entrer un choix valide",
            value_type="Sélection",
            assertions=["1", "q"]
        )

        # Récupèration des résultats quand le tournoi est terminé.
        if user_input == "1":
            rankings = play_tournament(tournament, loading_new_tournament=True)
        else:
            quit()

        # Affiche les résultats.
        print()
        print(f"Le tournoi {tournament.name} est terminé \nRésultats :")
        for i, player in enumerate(rankings):
            print(f"{str(i+1)} - {player}")
        # Mise à jour des classements
        print()
        user_input = self.user_entry(
            message_display="Mise à jour des classements\n"
                            "1 - Automatiquement\n"
                            "2 - Manuellement\n"
                            "q - Quitter\n> ",
            message_error="Veuillez entrer un choix valide",
            value_type="Sélection",
            assertions=["1", "2", "q"]
        )

        if user_input == "1":
            for i, player in enumerate(rankings):
                print(player.name)
                update_rankings(player, i+1)

        elif user_input == "2":
            for player in rankings:
                rank = self.user_entry(
                    message_display=f"classement de {player}:\n> ",
                    message_error="Veuillez entrer un nombre entier.",
                    value_type="numeric"
                )
                update_rankings(player, rank)

        else:
            quit()
