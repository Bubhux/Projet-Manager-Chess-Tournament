"""Module report_menu."""
from rich.console import Console
from rich.table import Table
from operator import itemgetter

from views.view_user_entry import ViewUserEntry
from controllers.database_controllers import DataBase


class Report(ViewUserEntry):
    """Class report."""

    def __init__(self):
        """Initialise un rapport."""
        database = DataBase()
        self.players = database.loading_database("players")
        self.tournaments = database.loading_database("tournaments")
        self.console = Console()

    def display_menu_players_reports(self, players=[]):
        """Affiche le menu pour le rapport des joueurs."""

        while True:
            # Affichage du classement.
            self.console.print()
            table = Table(title="Classement tournoi", title_justify="left")
            table.add_column("ID")
            table.add_column("Nom", style="bold magenta")
            table.add_column("Prénom", style="bold magenta")

            for i, player in enumerate(players, start=1):
                table.add_row(str(i), player['name'], player['surname'])

            self.console.print(table)
            print()

            players = players
            self.console.print("Voir les détails d'un joueur", style="bold blue")

            builded_selection = self.build_selection(
                iterable=players,
                display_message="",
                assertions=["r"]
            )

            user_input = self.user_entry(
                message_display=builded_selection['message'] + "r - Retour\n> ",
                message_error="Veuillez faire un choix valide.",
                value_type="Sélection",
                assertions=builded_selection['assertions']
            )

            if user_input == "r":
                break

            else:
                selected_player = players[int(user_input)-1]
                self.console.print()

                # Affichage des détails du joueur sélectionné.
                table = Table(
                    title=f"Détails du joueur {selected_player['name']} {selected_player['surname']}",
                    style="bold blue"
                )

                table.add_column("Attribut")
                table.add_column("Valeur")

                table.add_row("Rang:", str(selected_player['rank']))
                table.add_row("Score total:", str(selected_player['total_score']))
                table.add_row("Nom complet:", f"{selected_player['name']} {selected_player['surname']}")
                table.add_row("Date de naissance:", selected_player['birthday_date'])
                table.add_row("Sexe:", selected_player['sexe'])

                self.console.print(table)

                self.console.print("\nSélectionner", style="bold blue")
                self.console.print("r - Retour")

                user_input = self.user_entry(
                    message_display="> ",
                    message_error="Veuillez faire un choix valide.",
                    value_type="Sélection",
                    assertions=["r"]
                )

                if user_input == "r":
                    break

    def display_menu_tournaments_reports(self):
        """Affiche le menu pour les rapports de tournoi."""
        self.console.print()
        self.console.print("Voir les détails d'un tournoi", style="bold blue")

        builded_selection = self.build_selection(
            iterable=self.tournaments,
            display_message="",
            assertions=['r']
        )

        while True:
            # Affichage de tout les tournois.
            # Choix d'un tournoi afin d'en voir les détails.
            user_input = self.user_entry(
                message_display=builded_selection['message'] + "r - Retour\n> ",
                message_error="Veuillez faire un choix valide.",
                value_type="Sélection",
                assertions=builded_selection['assertions']
            )

            if user_input == "r":
                break

            else:
                selected_tournament = self.tournaments[int(user_input)-1]

                # Affichage des détails du tournoi choisi.
                table = Table(title=f"Détails du tournoi {selected_tournament['name']}")
                table.add_column("Attribut")
                table.add_column("Valeur")

                table.add_row("Nom", selected_tournament['name'])
                table.add_row("Lieu", selected_tournament['location'])
                table.add_row("Date", selected_tournament['date'])
                table.add_row("Contrôle du temps", selected_tournament['time_control'])
                table.add_row("Nombre de tours", str(selected_tournament['number_tours']))
                table.add_row("Description", selected_tournament['description'])

                self.console.print(table)

                self.console.print("\nSélectionner", style="bold blue")
                self.console.print("1 - Voir les participants")
                self.console.print("2 - Voir les tours")
                self.console.print("r - Retour")

                user_input = self.user_entry(
                    message_display="> ",
                    message_error="Veuillez entrer une sélection valide",
                    value_type="Sélection",
                    assertions=["1", "2", "r"]
                )

                if user_input == "r":
                    break

                elif user_input == "1":
                    while True:
                        self.console.print("\nType de classement", style="bold blue")
                        self.console.print("1 - Par rang")
                        self.console.print("2 - Par ordre alphabétique")
                        self.console.print("r - Retour")
                        self.console.print()

                        user_input = self.user_entry(
                            message_display="> ",
                            message_error="Veuillez entrer une sélection valide",
                            value_type="Sélection",
                            assertions=["1", "2", "r"]
                        )

                        if user_input == "r":
                            break
                        elif user_input == "1":
                            sorted_players = self.sort_players(selected_tournament["players"], by_rank=True)
                            self.display_menu_players_reports(players=sorted_players)
                        elif user_input == "2":
                            sorted_players = self.sort_players(selected_tournament["players"], by_rank=False)
                            self.display_menu_players_reports(players=sorted_players)

                elif user_input == "2":
                    self.display_menu_tours(selected_tournament["tours"])

    def display_menu_tours(self, tours: list):
        """Affiche le menu des détails d'un tour."""
        self.console.print()
        self.console.print("Voir les détails d'un tour", style="bold blue")

        builded_selection = self.build_selection(
            iterable=tours,
            display_message="",
            assertions=['r']
        )

        while True:
            console = Console()

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
                    table = Table(title=f"Détails du tour {selected_tour['name']}")
                    table.add_column("Attribut")
                    table.add_column("Valeur")

                    table.add_row("Nom", selected_tour['name'])
                    table.add_row("Nombre de matchs", str(len(selected_tour['matchs'])))
                    table.add_row("Date de début", selected_tour['time_start'])
                    table.add_row("Date de fin", selected_tour['time_end'])

                    console.print(table)

                    self.console.print("\nSélectionner", style="bold blue")
                    self.console.print("1 - Voir les matchs")
                    self.console.print("r - Retour")

                    user_input = self.user_entry(
                        message_display="> ",
                        message_error="Veuillez faire un choix valide",
                        value_type="Sélection",
                        assertions=["1", "r"]
                    )

                    if user_input == "r":
                        break

                    else:
                        self.console.print("\nVoir les détails d'un match", style="bold blue")

                        builded_selection = self.build_selection(
                            iterable=selected_tour['matchs'],
                            display_message="",
                            assertions=['r']
                        )

                        user_input = self.user_entry(
                            message_display=builded_selection['message'] + "r - Retour\n> ",
                            message_error="Veuillez faire un choix valide.",
                            value_type="Sélection",
                            assertions=builded_selection['assertions']
                        )

                        if user_input == "r":
                            break
                        else:
                            selected_match = selected_tour['matchs'][int(user_input) - 1]
                            while True:
                                table = Table(title=f"Détails du {selected_match['name']}")
                                table.add_column("Attribut")
                                table.add_column("Valeur")

                                table.add_row(
                                    "Joueur 1",
                                    f"{selected_match['player_1']['name']} {selected_match['player_1']['surname']} "
                                    f"({selected_match['score_player_1']} pts)"
                                )
                                table.add_row(
                                    "Joueur 2",
                                    f"{selected_match['player_2']['name']} {selected_match['player_2']['surname']} "
                                    f"({selected_match['score_player_2']} pts)"
                                )

                                # Récupération du prénom et du nom du gagnant
                                if selected_match['winner']:
                                    full_name = selected_match['winner']
                                    first_name, last_name = full_name.split()
                                    winner_name = f"[size=8]{first_name} {last_name}[/size]"
                                else:
                                    winner_name = "Pending"

                                table.add_row("Gagnant", winner_name)

                                console.print(table)

                                self.console.print("\nSélectionner", style="bold blue")
                                self.console.print("r - Retour 4")

                                user_input = self.user_entry(
                                    message_display="> ",
                                    message_error="Veuillez faire un choix valide",
                                    value_type="Sélection",
                                    assertions=["r"]
                                )

                                if user_input == "r":
                                    return Report().display_menu_tournaments_reports()

    @staticmethod
    def sort_players(players: list, by_rank: bool) -> list:
        """Trie les joueurs par le classement."""
        if by_rank:
            sorted_players = sorted(players, key=itemgetter('rank'))
        else:
            sorted_players = sorted(players, key=itemgetter('name'))

        return sorted_players
