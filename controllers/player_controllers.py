"""Module player_controllers."""
from rich.console import Console
from rich.table import Table

from views.player_menu import CreatePlayer
from models.player_models import Player
from controllers.database_controllers import DataBase


def create_player():
    """Fonction création de joueurs renvoie un joueur."""
    database = DataBase()

    # Récupération des données du joueur.
    user_data = CreatePlayer().display_create_player_menu()

    # Création du joueur.
    player = Player(
        user_data['name'],
        user_data['surname'],
        user_data['birthday_date'],
        user_data['sexe'],
        user_data['rank'],
        user_data['total_score'])

    serialized_player = player.serialized_player()
    print(serialized_player)

    database.save_database("players", serialized_player)

    return player


def update_rankings(player, rank, score=True):
    """Fonction de mise à jour du classement."""
    database = DataBase()

    if score:
        player.total_score += player.tournament_score

    player.rank = rank
    serialized_player = player.serialized_player(save_tournament_score=True)
    database.update_player_rank("players", serialized_player)

    # Création de la table
    table = Table(title="Mise à jour du rang", style="bold magenta")
    table.add_column("Attribut")
    table.add_column("Valeur")

    table.add_row("Joueur", str(player))
    table.add_row("Score total", f"{player.total_score} pts")
    table.add_row("Rang", str(player.rank))

    # Affichage de la table
    console = Console()
    console.print(table)
    console.print("---------------------------------------------------------------")
