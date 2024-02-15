"""Module database_controllers."""
from pathlib import Path
from tinydb import TinyDB
from tinydb import where
from rich.console import Console

from models.tournament_models import Tournament
from models.player_models import Player
from models.tour_models import Tour
from models.match_models import Match


class DataBase:
    """Class Database."""

    def __init__(self):
        self.console = Console()

    def save_database(self, database_name, serialized_data):
        """Fonction de création de fichiers de sauvegarde pour les tournois et les joueurs."""
        Path("save data/").mkdir(exist_ok=True)
        try:
            db = TinyDB(f"save data/{database_name}.json")
        except FileNotFoundError:
            with open(f"save data/{database_name}.json", "w"):
                pass
            db = TinyDB("save data/" + database_name + ".json")

        db.insert(serialized_data)
        self.console.print("[bold green]Sauvegarde, mise à jour effectuée avec succès.[/bold green]\n")

    def update_tournament_database(self, database_name, serialized_data):
        """Fonction de sauvgarde pour les tournois vers la base de donées."""
        db = TinyDB(f"save data/{database_name}.json")
        db.update(
            serialized_data,
            where("name") == serialized_data["name"]
        )
        self.console.print(
            f"[bold green]Tournoi {serialized_data['name']} "
            f"sauvegardé, mise à jour effectuée avec succès.[/bold green]\n"
        )

    def update_player_rank(self, database_name, serialized_data):
        """Fonction de sauvgarde pour les joueurs vers la base de donées."""
        db = TinyDB(f"save data/{database_name}.json")
        db.update(
            {"rank": serialized_data["rank"], "total_score": serialized_data["total_score"]},
            where("name") == serialized_data["name"]
        )
        self.console.print(
            f"[bold green]Joueur {serialized_data['name']} {serialized_data['surname']} sauvegardé, "
            f"mise à jour effectuée avec succès.[/bold green]\n"
        )

    def loading_database(self, database_name):
        """Fonction pour charger les sauvegardes de la base de données."""
        try:
            db = TinyDB(f"save data/{database_name}.json")
            return db.all()
        except FileNotFoundError:
            return None

    def loading_player(self, serialized_player, loading_tournament_score=False):
        """Charge un joueur."""
        player = Player(
            serialized_player['name'],
            serialized_player['surname'],
            serialized_player['birthday_date'],
            serialized_player['sexe'],
            serialized_player['rank'],
            serialized_player['total_score']
        )
        if loading_tournament_score:
            player.tournament_score = serialized_player['tournament_score']

        return player

    def loading_tournament(self, serialized_tournament):
        """Charge un tournoi."""
        load_tournament = Tournament(
            serialized_tournament["name"],
            serialized_tournament["location"],
            serialized_tournament["date"],
            serialized_tournament["time_control"],
            [self.loading_player(
                player, loading_tournament_score=True
            ) for player in serialized_tournament["players"]],
            serialized_tournament["description"],
            serialized_tournament["number_tours"]
        )
        load_tournament.tour = self.loading_tours(serialized_tournament, load_tournament)

        return load_tournament

    def loading_tours(self, serialized_tournament, tournament):
        """Charge un tours."""
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
            load_tour = Tour(tour['name'], pairs_players, loading_match=True)

            load_tour.matchs = [self.loading_matchs(match, tournament) for match in tour['matchs']]
            load_tour.time_start = tour['time_start']
            load_tour.time_end = tour['time_end']
            load_tours.append(load_tour)

        return load_tours

    def loading_matchs(self, serialized_match, tournament):
        """Charge un match."""
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
