from views.player_menu import CreatePlayer
from models.player_models import Player 


def create_player():

    # Récupération des données du joueur
    user_data = CreatePlayer().display_create_player_menu()

    # Création du joueur
    player = Player(
        user_data["surname"],
        user_data["name"],
        user_data["date_of_birth"],
        user_data["sexe"],
        user_data["total_score"],
        user_data["rank"])

    return player
