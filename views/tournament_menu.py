from views.view_user_entry import ViewUserEntry, display_check_timestamp


class CreateTournament(ViewUserEntry):

    def display_tournament_menu(self):

        date = display_check_timestamp()
        print( date + " : Nouveau tournoi")

        name = input("Nom du tournoi :\n> ")
        description = input("Description du tournoi :\n> ")

        location = self.user_entry(
            message_display = "Lieu :\n> ",
            message_error = "Entrer un lieu valide",
            value_type = "string"
        )

        user_selection_time = self.user_entry(
            message_display = "Contrôle de temps :\n0 - Bullet\n1 - Blitz\n2 - Coup rapide\n> ",
            message_error = "Veuillez entrer 0, 1 ou 2",
            value_type = "Sélection",
            assertions = ["0", "1", "2"]
        )

        if user_selection_time == "0":
            time_control = "Bullet"
        elif user_selection_time == "1":
            time_control = "Blitz"
        else:
            time_control = "Coup rapide"

        number_players = self.user_entry(
            message_display = "Nombre de joueurs :\n> ",
            message_error = "Veuillez entrer un nombre entier supérieur à 1 ou 2",
            value_type = "numeric_superior",
            defaut_value = 2
        )

        number_rounds = self.user_entry(
            message_display = "Nombre de tours (4 par défaut) :\n> ",
            message_error = "Veuillez entrer 4 ou plus",
            value_type = "numeric_superior",
            defaut_value = 4
        )

        return {
            "name": name,
            "location": location,
            "date": date,
            "time_control": time_control,
            "number_players": number_players,
            "number_rounds": number_rounds,
            "description": description
        }


def test_main():

     create_tournament = CreateTournament()
     create_tournament.display_tournament_menu()


if __name__ == "__main__":
    test_main()


