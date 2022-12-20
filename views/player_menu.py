from views.view_user_entry import ViewUserEntry


class CreatePlayer(ViewUserEntry):
    """Player view."""
    def display_create_player_menu(self):
        
        """Saisie pour le prénom."""
        name = input("Tapez le prénom du joueur : ")
        #if not name:
        #    return None
        #return name

        """Saisie pour le nom."""
        surname = input("Tapez le nom du joueur : ")
        #if not surname:
        #    return None
        #return surname

        """Saisie pour la date d'anniversaire."""
        date_of_birdh_input = input("Tapez la date de naissance du joueur : ")

        date_of_birdh = self.user_entry(
            message_display = "Date de naissance (format DD/MM/YYYY):\n> ",
            message_error = "Veuillez entrer une date au format valide : DD/MM/YYYY",
            value_type = "date"
        )

        #if not date_of_birdh:
        #    return None
        #return date_of_birdh

        """Saisie pour le classement."""
        rank_input = input("Tapez le classement du joueur : ")

        rank = self.user_entry(
            message_display = "Rang\n> ",
            message_error ="Veuillez entrer une valeur numérique valide",
            value_type = "numeric"
        )

        #if not rank:
        #    return None
        #return rank

        print(f"Le joueur {name} {surname} est créé")

        return {
            "name": name,
            "surname": surname,
            "date_of_birdh": date_of_birdh,
            "rank": rank,
        }


def test_main():

    create_player = CreatePlayer()
    create_player.display_create_player_menu()


if __name__ == "__main__":
    test_main()
