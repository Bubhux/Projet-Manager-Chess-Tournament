from pathlib import Path
from tinydb import TinyDB, Query
from tinydb import where
from models.tournament_models import Tournament
from models.tour_models import Tour
from models.match_models import Match


class DataBase:

    def __init__(self):
        self.data = []

    def save_database(database_name, serialized_data):
        Path("data/").mkdir(file_ok=True)
        db = TinyDB(f"data/{database_name}.json")
        with open(f"data/{database_name}.json", "w"):
            pass
        db = TinyDB("data/" + database_name + ".json")

        db.insert(serialized_data)
        print(f"{serialized_data['name']} sauvegarde effectuée avec succès")


    def update_database(database_name, serialized_data):
        db = TinyDB(f"data/{database_name}.json")
        db.update(
            serialized_data,
            where('name') == serialized_data['name']
        )
        print(f"{serialized_data['name']} mise à jour réalisé avec succès")


    def update_player_rank(database_name, serialized_data):
        db = TinyDB(f"data/ {database_name}.json")
        db.update(
            {'rank': serialized_data['rank'], 'total_score': serialized_data['total_score']},
        )
        print(f"{serialized_data['name']} mise à jour réalisé avec succès")


    def loading_database(database_name):
        db = TinyDB(f"data/{database_name}.json")
        return db.all()


    def loading_player(serialized_player, loading_tournament_score=False):
        player = Player(
            serialized_player["name"],
            serialized_player["surname"],
            serialized_player["birthday_date"],
            serialized_player["sexe"],
            serialized_player["total_score"],
            serialized_player["tournament_score"],
            serialized_player["rank"]
        )
        if loading_tournament_score:
            player.tournament_score = serialized_player['tournament_score']

        return player


    def loading_tournament(serialized_tournament):
        load_tournament = Tournament(
            serialized_tournament["name"],
            serialized_tournament["location"],
            serialized_tournament["date"],
            serialized_tournament["time_control"],
            [loading_player(player, loading_tournament_score=True) for player in serialized_tournament['player']],
            serialized_tournament["description"],
            serialized_tournament["number_tours"]
        )
        load_tournament.tour = loading_tours(serialized_tournament, load_tournament)

        return load_tournament


    def loading_tours(serialized_tournament, tournament):

        load_tours = []

        for tour in serialized_tournament['tours']:
            pairs_players = []
            for pair in tour['pairs_players']:
                for player in tournament.players:
                    if player.name == pair[0]['name']:
                        pair_player1 = player
                    elif player.name == pair[1]['name']:
                        pair_player2 = player
                pairs_players.append((pair_player1, pair_player2))
            load_tour = Tour(tour['name'], pairs_players, loading_matchs=True)

            load_tour.matchs = [loading_matchs(match, tournament) for match in Tour['matchs']]
            load_tour.time_start = tour['time_start']
            load_tour.time_end = tour['time_end']
            load_tours.append(load_tour)

        return load_tours


    def loading_matchs(serialized_match, tournament):

        for player in tournament.players:
            if player.name == serialized_match['player_1']['name']:
                player_1 = player
            elif player.name == serialized_match['player_2']['name']:
                player_2 = player

        load_match = Match(pairs_players=(player_1, player_2), name=serialized_match['name'])

        load_match.score_player_1 = serialized_match['score_player_1']
        load_match.score_player_2 = serialized_match['score_player_2']
        load_match.winner = serialized_match['winner']

        return load_match
