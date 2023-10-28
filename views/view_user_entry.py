"""Module view_user_entry."""
from datetime import datetime


class ViewUserEntry:
    """Class des entrées de valeur saisie."""
    def user_entry(self, message_display, message_error, value_type, assertions=None, defaut_value=None):
        """Fonction des entrées de saisie."""
        while True:
            value_input = input(message_display)
            if value_type == "numeric":
                if value_input.isnumeric():
                    value_input = int(value_input)
                    return value_input
                else:
                    print(message_error)
                    continue

            if value_type == "numeric_superior":
                if value_input.isnumeric():
                    value_input = int(value_input)
                    if value_input >= defaut_value:
                        return value_input
                    else:
                        print(message_error)
                        continue
                else:
                    print(message_error)
                    continue

            if value_type == "string":
                try:
                    float(value_input)
                    print(message_error)
                    continue
                except ValueError:
                    return value_input
            elif value_type == "date":
                if self.verification_date(value_input):
                    return value_input
                else:
                    print(message_error)
                    continue
            elif value_type == "Sélection":
                if value_input in assertions:
                    return value_input
                else:
                    print(message_error)
                    continue

    @staticmethod  # Atttirbut statique.
    def verification_date(value_test):
        """Vérifie la saisie de la date de naissance."""
        if "/" not in value_test:
            return False
        else:
            split_date = value_test.split("/")
            for date in split_date:
                if not date.isnumeric():
                    return False
            return True

    @staticmethod  # Atttirbut statique.
    def build_selection(iterable: list, display_message: str, assertions: list) -> dict:
        """Itére sur une liste renvoi un message et une assertion."""
        display_message = display_message
        assertions = assertions

        for i, data in enumerate(iterable):
            display_message = display_message + f"{i+1} - {data['name']}\n"
            assertions.append(str(i+1))

        return {
            "message": display_message,
            "assertions": assertions
        }

    def display_check_timestamp(self):
        """Retourne l'heure et la date."""
        return datetime.now().strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
