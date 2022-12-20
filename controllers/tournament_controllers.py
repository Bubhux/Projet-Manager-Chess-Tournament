from models.tournament_models import Tournament
from views.tournament_menu import CreateTournament
from views.view_user_entry import ViewUserEntry
from controllers.player_controllers import create_player


def create_tournament():

    menu = ViewUserEntry()

    # Récupération des données du tournoi
    user_entries = CreateTournament().display_tournament_menu()

    # Choix chargement des joueurs
    user_input = menu.user_entry(
        message_display="Sélectionner\n0 - Créer des joueurs\n1 - Charger des joueurs\n> ",
        message_error="Entrer un choix valide",
        value_type="Sélection",
        assertions=["0", "1"]
    )

    # Chargement des joueurs
    if user_input == "1":
        players = []
        user_input = menu.user_entry(
            message_display="Combien de joueurs a charger ?\n> ",
            message_error="Entrer 0 ou 1",
            value_type="numeric"
        )

    # Création des joueurs
    else:
        print(f"Création de {str(user_entries['number_players'])} joueurs")
        players = []
        while len(players) < user_entries["number_players"]:
            players.append(create_player())

    # Création du tournoi
    tournament = Tournament(
        user_entries["name"],
        user_entries["location"],
        user_entries["date"],
        user_entries["time_control"],
        players,
        user_entries["description"],
        user_entries["number_tours"]
    )

    return tournament

def play_tournament(tournament, load_new_tournament=False):

	menu = ViewUserEntry()

	print(f"Début du tournoi {tournament.name}")

	while True:

		# Calcul des tours restant à jouer pour un nouveau tournoi
		z = 0 
		if load_new_tournament:
			for round in tournament.tours:
				if round.time_end == "":
					z += 1
				number_tours_play = tournament.number_tours - z
				load_new_tournament = False
			else:
				number_tours_play = tournament.number_tours

			for i in range(number_tours_play):
				# Création du tour
				tournament.create_tours(tour_number=i+z)

				# Joue le dernier tour créé
				current_tour = tournament.tours[-1]
				print(current_tour.time.start + " : Début du " + current_tour.name)

				# Le tour terminé on passe au tour suivant
				while True:
					user_input = menu.user_entry(
						message_display = "Sélectionner\n"
										  "0 - Tour suivant\n"
										  "1 - Afficher les classements\n",
						message_error = "Sélectionner un choix",
						value_type = "Sélection",
						assertions = ["0", "1"]
					)
					print()

					# Tour suivant 
					if user_input == "0":
						current_tour.match_completed()
						break

					# Affiche les classements 
					elif user_input == "1":
						print(f"Classement du tournoi {tournament.name}\n")
						for i, player in enumerate(tournament.get_ranking()):
							print(f"{str(i + 1)} - {player}")

				if load_new_tournament:
					break

			if load_new_tournament:
				continue 

			else:
				break




