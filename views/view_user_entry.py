import time
from datetime import datetime


class ViewUserEntry:

    def user_entry(self, message_display, message_error, value_type, assertions=None, defaut_value=None):
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

    @staticmethod
    def verification_date(value_test):
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
        display_message = display_message
        assertions = assertions

        for i, data in enumerate(iterable):
            display_message = display_message + f"{i+1} - {data['name']}\n"
            assertions.append(str(i+1))

        return {
            "message": display_message,
            "assertions": assertions
            }

def display_check_timestamp():
    return datetime.now().strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
           #time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))


class DisplayFrame:

    def display_data_frame(self, data, index=None, columns=None):
        display_frame = pd.DataFrame(self, data, index, columns)
        print("Les données que vous avez entrer :")
        print(display_frame)


class DisplayTour:

    def __init__(self):
        self.match = match_models.Match()

    def display_tour(self, tour_name, list_matchs):

        print(f"---------------------{tour_name}---------------------\n")
        print()
        for match in list_matchs:
            print(match)
            print()

    def display_tour_time(self):
        print()
        input("Appuyez sur une touche pour commencer le tour")
        print()
        time_start = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f"Début du tour : {time_start}")
        print()
        input("Appuyez sur une touche lorsque le tour est terminé")
        time_end = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f"Fin du tour : {time_end}")
        print()
        return time_start, time_end