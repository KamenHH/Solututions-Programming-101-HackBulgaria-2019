import sys
from controller.start_controller import StartController
from utils.constants import Constants
from utils.decorators import Clear


class StartMenu:
    MENU = {
        '1': StartController.sign_in,
        '2': StartController.sign_up,
        '3': StartController.exit_app
        }

    @classmethod
    def run(cls):
        # print('Welcome!')
        while True:
            StartMenu.print_menu(Constants.START_MENU_OPTIONS)
            user_choice = input(Constants.PROMPT)
            user_obj = cls.MENU.get(user_choice, cls.default)()
            if user_obj:
                return user_obj

    @staticmethod
    def default():
        print('No such option!')

    @staticmethod
    @Clear
    def print_menu(menu):
        print(menu)
