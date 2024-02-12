"""Module view_user_entry."""
from datetime import datetime
from rich.table import Table
from rich.console import Console


class ViewUserEntry:
    """Class des entrées de valeur saisie."""

    def user_entry(self, message_display, message_error, value_type, assertions=None, default_value=None):
        """Fonction des entrées de saisie."""
        while True:
            value_input = input(message_display)
            is_valid = self.validate_input(value_input, value_type, assertions, default_value)
            if is_valid:
                return value_input
            else:
                print(message_error)

    def validate_input(self, value_input, value_type, assertions=None, default_value=None):
        """Valide l'entrée utilisateur en fonction du type spécifié."""
        if value_type == "numeric":
            return self.validate_numeric(value_input)
        elif value_type == "numeric_superior":
            return self.validate_numeric_superior(value_input, default_value)
        elif value_type == "string":
            return self.validate_string(value_input)
        elif value_type == "date":
            return self.validate_date(value_input)
        elif value_type == "Sélection":
            return self.validate_selection(value_input, assertions)
        else:
            return False

    def validate_numeric(self, value_input):
        """Valide une valeur numérique."""
        return value_input.isnumeric()

    def validate_numeric_superior(self, value_input, default_value):
        """Valide une valeur numérique supérieure à une valeur par défaut."""
        return value_input.isnumeric() and int(value_input) >= default_value

    def validate_string(self, value_input):
        """Valide une chaîne de caractères."""
        try:
            float(value_input)
            return False
        except ValueError:
            return True

    def validate_date(self, value_input):
        """Valide une date."""
        return self.verification_date(value_input)

    def validate_selection(self, value_input, assertions):
        """Valide une sélection."""
        return value_input in assertions

    @staticmethod
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

    @staticmethod
    def build_selection(iterable: list, display_message: str, assertions: list) -> dict:
        """Itére sur une liste renvoi un message et une assertion."""
        console = Console()
        table = Table(title="Sélectionner", title_justify="left")
        table.add_column("ID")
        table.add_column("Nom complet")

        for i, data in enumerate(iterable):
            if 'surname' in data:
                table.add_row(str(i+1), f"{data['name']} {data['surname']}")
            else:
                table.add_row(str(i+1), data['name'])

            assertions.append(str(i+1))

        console.print(table)

        return {
            "message": display_message,
            "assertions": assertions
        }

    @staticmethod
    def display_check_timestamp():
        """Retourne l'heure et la date."""
        return datetime.now().strftime("%d/%m/%Y - %Hh%Mm%Ss")
