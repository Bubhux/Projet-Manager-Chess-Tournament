"""Module tournament_controllers."""
from rich.console import Console
from rich.table import Table
from models.tournament_models import Tournament
from views.view_user_entry import ViewUserEntry
from views.tournament_menu import CreateTournament, LoadingTournament
from views.player_menu import LoadindPlayer
from controllers.player_controllers import create_player, update_rankings
from controllers.database_controllers import DataBase


def create_tournament():
    """Fonction création de tournoi."""
    menu = ViewUserEntry()
    database = DataBase()
    console = Console()

    # Récupération des données du tournoi.
    user_data = CreateTournament().display_tournament_menu()

    # Choix chargement des joueurs.
    console.print("[bold]Sélectionner[/bold]\n1 - Créer des joueurs\n2 - Charger des joueurs")

    user_input = menu.user_entry(
        message_display="> ",
        message_error="Entrer un choix valide",
        value_type="Sélection",
        assertions=["1", "2"]
    )

    # Chargement des joueurs.
    if user_input == "2":
        players = []
        user_input = menu.user_entry(
            message_display="Combien de joueurs à charger ?\n> ",
            message_error="Entrer 0 ou 1",
            value_type="numeric"
        )
        serialized_players = LoadindPlayer().display_loading_player(
            number_players_loading=user_input
        )
        for serialized_player in serialized_players:
            player = database.loading_player(serialized_player)
            players.append(player)

    # Création des joueurs.
    else:
        console.print(f"Création de {str(user_data['number_players'])} joueurs")

        players = [create_player() for _ in range(int(user_data['number_players']))]

    # Création du tournoi.
    tournament = Tournament(
        user_data['name'],
        user_data['location'],
        user_data['date'],
        user_data['time_control'],
        players,
        user_data['description'],
        user_data['number_tours'])
    database.save_database("tournaments", tournament.serialized_tournament())

    return tournament


def play_tournament(tournament, loading_new_tournament=False):
    """Affiche le début du tournoi."""
    menu = ViewUserEntry()
    database = DataBase()
    console = Console()

    console.print(f"Début du tournoi {tournament.name}")
    console.print()

    while True:
        # Calcul des tours restants à jouer pour un nouveau tournoi.
        z = 0
        if loading_new_tournament:
            for tour in tournament.tours:
                if tour.time_end == "":
                    z += 1
            number_tours_play = tournament.number_tours - z
            loading_new_tournament = False
        else:
            number_tours_play = tournament.number_tours

        for i in range(number_tours_play):
            # Création du tour.
            tournament.create_tour(tour_number=i+z)

            # Joue le dernier tour créé.
            current_tour = tournament.tours[-1]
            console.print(current_tour.time_start + " : Début du " + current_tour.name)

            # Le tour terminé on passe au tour suivant.
            while True:
                console.print("\nSélectionner", style="bold blue")
                console.print("1 - Tour suivant")
                console.print("2 - Afficher les classements")
                console.print("3 - Mettre à jour les classements")
                console.print("4 - Sauvegarder le tournoi")
                console.print("5 - Charger un tournoi")

                user_input = menu.user_entry(
                    message_display="> ",
                    message_error="Sélectionner un choix",
                    value_type="Sélection",
                    assertions=["1", "2", "3", "4", "5"]
                )
                console.print()

                # Tour suivant.
                if user_input == "1":
                    current_tour.match_completed()
                    break

                # Affiche les classements.
                elif user_input == "2":
                    console.print(f"Classement du tournoi {tournament.name}\n", style="bold green")
                    table = Table(title="Classement", title_justify="left")
                    table.add_column("Position", justify="center", style="bold magenta")
                    table.add_column("Joueur", justify="center", style="bold magenta")
                    for i, player in enumerate(tournament.tournament_rankings()):
                        table.add_row(str(i+1), f"Joueur {player}")

                    # Modifie le style des titres des colonnes
                    table.columns[0].header_style = "bold white"
                    table.columns[1].header_style = "bold white"
                    console.print(table)
                    console.print()

                # Changement des rangs.
                elif user_input == "3":
                    for player in tournament.players:
                        rank = menu.user_entry(
                            message_display=f"Classement du joueur {player}:\nSaisir le nouveau rang > ",
                            message_error="Veuillez entrer un nombre entier.",
                            value_type="numeric"
                        )
                        update_rankings(player, rank, score=False)
                    console.print()

                # Sauvegarder le tournoi.
                elif user_input == "4":
                    rankings = tournament.tournament_rankings()
                    for i, player in enumerate(rankings):
                        for x_player in tournament.players:
                            if player.name == x_player.name:
                                x_player.rank = str(i+1)
                    database.update_tournament_database("tournaments",
                                                        tournament.serialized_tournament(save_tours=True))

                # Charger un tournoi.
                elif user_input == "5":
                    serialized_loading_tournament = LoadingTournament().display_loading_tournament_menu()
                    tournament = database.loading_tournament(serialized_loading_tournament)
                    loading_new_tournament = True
                    break
            if loading_new_tournament:
                break
        if loading_new_tournament:
            continue
        else:
            break

    rankings = tournament.tournament_rankings()
    for i, player in enumerate(rankings):
        for x_player in tournament.players:
            if player.name == x_player.name:
                x_player.total_score += player.tournament_score
                x_player.rank = str(i+1)
    database.update_tournament_database("tournaments", tournament.serialized_tournament(save_tours=True))

    return rankings
