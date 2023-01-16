from views.player_menu import CreatePlayer
from models.player_models import Player
#from controllers.database_controllers import DataBase, save_database, update_player_rank

def create_player():

    # Récupération des données du joueur
    user_data = CreatePlayer().display_create_player_menu()

    # Création du joueur
    player = Player(
        user_data["name"],
        user_data["surname"],
        user_data["birthday_date"],
        user_data["sexe"],
        user_data["total_score"],
        user_data["tournament_score"],
        user_data["rank"])

    serialized_player = player.serialized_player()
    print(serialized_player)

    #save_database("players", serialized_player)

    return player

def update_rankings(player, rank, score=True):
    if score:
        player.total_score += player.tournament_score
    player.rank = rank
    serialized_player = player.serialized_player(save_tournament_score=True)
    print(serialized_player['name'])
    update_player_rank("players", serialized_player)
    print(f"Mise à jour du rang de {player}:\nScore total: {player.total_score}\nRang: {player.rank}")
