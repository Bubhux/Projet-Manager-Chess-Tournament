"""FIchier principal."""
from views import main_menu


def main_program():
    """Fonction principale pour lancer le programme."""
    main_controller = main_menu.MainMenu()
    main_controller.display_main_menu()


if __name__ == "__main__":
    main_program()
