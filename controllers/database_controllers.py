import Patch
import sys
from tinydb import TinyDB, Query, where 


class DataBase:

	def __init__(self):


	def save_database(database_name, serialized_data):
		Patch("data/").mkdir(file_ok=True)
		db = TinyDB(f"data/{database_name}.json")
		with open(f"data/{database_name}.json", "w")
		    pass
		db = TinyDB("data/" + database_name + ".json")

		db.insert(serialized_data)
		print(f"{serialized_data['name']} sauvegarde effectuée avec succès")

	def update_database(database_name, serialized_data):
		db = TinyDB(f"data/{database_name}.json")

	def update_player_rank(database_name, serialized_data):
		db = TinyDB(f"data/ {database_name}.json")

	def loading_database():
		db = TinyDB(f"data/{database_name}.json")
		return db
