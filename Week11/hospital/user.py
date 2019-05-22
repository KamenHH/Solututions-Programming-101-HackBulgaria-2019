from utils.constants import Constants
from database_layer.db_manager import DBManager
from hospital.user_validation import UserValidation


class User:
    db = DBManager()

    def __init__(self, username, password, salt):
        self.username = username
        self._password = password
        self._salt = salt

    def get_data(self):
        return self.__dict__.values()

    @classmethod
    def add_to_db(cls, user_instance):
        if isinstance(user_instance, Doctor):
            cls.db.add_user(Constants.DOCTOR_STR, *user_instance.get_data())
        else:
            cls.db.add_user(Constants.PATIENT_STR, *user_instance.get_data())


    @classmethod
    def find(cls, username, password):
        return cls.db.find_user(username, password)


class Doctor(User):
    def __init__(self, username, password, salt, doctor_type):
        super().__init__(username, password, salt)
        self.doctor_type = doctor_type


class Patient(User):
    def __init__(self, username, password, salt, age, address):
        super().__init__(username, password, salt)
        self.age = age
        self.address = address
