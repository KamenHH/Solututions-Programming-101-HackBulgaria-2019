import sys
from controller.input_manager import InputManager
from utils.decorators import Clear
from utils.constants import Constants
from hospital.user import User, Doctor, Patient


class StartController:

    @classmethod
    @Clear
    def sign_up(cls):
        user_type = InputManager.read_user_type()
        username = InputManager.read_username(sign_up=True)
        password, salt = InputManager.read_password(sign_up=True)

        if user_type == Constants.DOCTOR_STR:
            return cls.doctor_sign_up(username, password, salt)
        else:
            return cls.patient_sign_up(username, password, salt)
        return None

    @staticmethod
    def doctor_sign_up(username, password, salt):
        doctor_type = InputManager.read_doctor_type()
        doctor_obj = Doctor(username, password, salt, doctor_type)
        User.add_to_db(doctor_obj)
        return Constants.DOCTOR_STR, doctor_obj

    @staticmethod
    def patient_sign_up(username, password, salt):
        age = InputManager.read_age()
        address = InputManager.read_address()
        patien_obj = Patient(username, password, salt, age, address)
        User.add_to_db(patien_obj)
        return Constants.PATIENT_STR, patien_obj

    @staticmethod
    @Clear
    def sign_in():
        username = InputManager.read_username()
        password = InputManager.read_password(username=username) 
        user_data = User.find(username, password)
        if user_data:
            if user_data[0] == Constants.DOCTOR_STR:
                return Constants.DOCTOR_STR, Doctor(*user_data[1:])
            else:
                return Constants.PATIENT_STR, Patient(*user_data[1:])
        print('Incorrect username or password!')
        return None

        
    @staticmethod
    @Clear
    def exit_app(code=0):
        print('\nGoodbye!\n')
        sys.exit(code)