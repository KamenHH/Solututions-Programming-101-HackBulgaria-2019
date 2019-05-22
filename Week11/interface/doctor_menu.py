import sys
from utils.constants import Constants
from controller.doctor_controller import DoctorController
from utils.decorators import Clear


class DoctorMenu:
    MENU = {
        '5': DoctorController.return_to_login_screen
    }

    @classmethod
    def run(cls):
        # print('Login succesfull!')
        while True:
            DoctorMenu.print_menu(Constants.DOCTOR_MENU_OPTIONS)
            doctor_choice = input(Constants.PROMPT)
            return_bool = cls.MENU.get(doctor_choice, cls.default)()
            if not return_bool:
                return None

    @staticmethod
    def default():
        print('No such option!')

    @staticmethod
    @Clear
    def print_menu(menu):
        print(menu)
