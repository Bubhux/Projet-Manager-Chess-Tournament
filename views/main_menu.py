"""Module main_menu."""
from rich.console import Console
from rich.table import Table
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
        console = Console()
        database = DataBase()

        while True:
            console.print("\nSélectionner", style="bold blue")
            console.print("1 - Créer un tournoi")
            console.print("2 - Créer des joueurs")
            console.print("3 - Charger un tournoi")
            console.print("4 - Voir les rapports")
            console.print("q - Quitter")

            user_input = self.user_entry(
                message_display="> ",
                message_error="Entrer une valeur valide",
                value_type="Sélection",
                assertions=["1", "2", "3", "4", "q"]
            )
            console.print()

            # Créer un tournoi.
            if user_input == "1":
                tournament = create_tournament()
                break

            # Créer des joueurs.
            elif user_input == "2":
                num_players = int(self.user_entry(
                    message_display="Nombre de joueurs à créer :\n> ",
                    message_error="Entrer une valeur numérique valide ",
                    value_type="numeric"
                ))
                for _ in range(num_players):
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
                    console.print("Aucun tournoi sauvegardé.", style="bold red")
                    continue

            # Voir les rapports.
            elif user_input == "4":
                report_choice = None
                while report_choice != "r":
                    console.print("1 - Joueurs")
                    console.print("2 - Tournois")
                    console.print("r - Retour")

                    report_choice = self.user_entry(
                        message_display="> ",
                        message_error="Veuillez faire un choix valide.",
                        value_type="Sélection",
                        assertions=["1", "2", "r"]
                    )
                    console.print()

                    if report_choice == "1":
                        ranking_choice = None
                        while ranking_choice != "r":
                            console.print()
                            console.print("Voir le classement", style="bold blue")
                            console.print("1 - Par rang")
                            console.print("2 - Par ordre alphabétique")
                            console.print("r - Retour")
                            console.print()

                            ranking_choice = self.user_entry(
                                message_display="> ",
                                message_error="Veuillez faire un choix valide.",
                                value_type="Sélection",
                                assertions=["1", "2", "r"]
                            )

                            if ranking_choice == "1":
                                sorted_players = Report().sort_players(Report().players, by_rank=True)
                                Report().display_menu_players_reports(players=sorted_players)
                            elif ranking_choice == "2":
                                sorted_players = Report().sort_players(Report().players, by_rank=False)
                                Report().display_menu_players_reports(players=sorted_players)
                            elif ranking_choice == "r":
                                break
                    elif report_choice == "2":
                        try:
                            Report().display_menu_tournaments_reports()
                        except TypeError:
                            console.print("Aucun tournoi sauvegardé.", style="bold red")
            else:
                quit()

        # Lancement du tournoi.
        console.print("\nSélectionner", style="bold blue")
        console.print("1 - Jouer le tournoi")
        console.print("q - Quitter")

        user_input = self.user_entry(
            message_display="> ",
            message_error="Veuillez entrer un choix valide",
            value_type="Sélection",
            assertions=["1", "q"]
        )

        # Récupération des résultats quand le tournoi est terminé.
        if user_input == "1":
            rankings = play_tournament(tournament, loading_new_tournament=True)
        else:
            quit()

        # Affiche les résultats.
        console.print(f"\nLe tournoi {tournament.name} est terminé", style="bold green")
        table = Table(title="Résultats", title_justify="left")
        table.add_column("Position", style="bold magenta")
        table.add_column("Joueur", justify="center", style="bold magenta")

        for i, player in enumerate(rankings):
            table.add_row(str(i + 1), str(player))

        # Modifie le style des titres des colonnes
        table.columns[0].header_style = "bold white"
        table.columns[1].header_style = "bold white"
        console.print(table)

        # Mise à jour des classements
        console.print("\nMise à jour des classements", style="bold blue")
        console.print("1 - Automatiquement")
        console.print("2 - Manuellement")
        console.print("q - Quitter")

        user_input = self.user_entry(
            message_display="> ",
            message_error="Veuillez entrer un choix valide",
            value_type="Sélection",
            assertions=["1", "2", "q"]
        )

        if user_input == "1":
            for i, player in enumerate(rankings):
                update_rankings(player, i + 1)

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
