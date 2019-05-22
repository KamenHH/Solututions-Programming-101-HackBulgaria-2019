import sys
import os
from utils.constants import Constants
from interface.start_menu import StartMenu
from interface.doctor_menu import DoctorMenu


class Application:
    
    @classmethod
    def start(cls):
        while True:
            user_data = StartMenu.run()
            if user_data[0] == Constants.DOCTOR_STR:
                DoctorMenu.run()
            elif user_data[0] == Constants.PATIENT_STR:
                pass

if __name__ == "__main__":
    Application.start()

# from controller.input_manager import InputManager
# from controller.main_controller import MainController

# if __name__ == "__main__":
#     print(MainController.sign_up())
    