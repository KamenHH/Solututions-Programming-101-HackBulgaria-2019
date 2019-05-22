import os
import sqlite3


class Constants:
    PROMPT = '>'

    DB_NAME = os.path.join('database_layer', 'hospital.db') 
    DB_ENIGNE = sqlite3

    DOCTOR_STR = 'Doctor'
    PATIENT_STR = 'Patient'
    USER_TYPES = [DOCTOR_STR, PATIENT_STR]

    USERNAME_MIN_SIZE = 3
    USERNAME_MAX_SIZE = 25
    PASSWORD_MIN_SIZE = 8
    PASSWORD_MAX_SIZE = 25
    ADDRESS_MAX_SIZE = 50

    START_MENU_OPTIONS = """\
1 - sign in
2 - sign up
3 - exit"""

    DOCTOR_MENU_OPTIONS = """\
1 - check schedule
2 - check reserved appointments
3 - check appointments for a given date
4 - reschedule appoinment
5 - exit
    """

    SYMBOLS_FOR_SALT = """
    !@#$%^&*-=()"""

    SALT_SIZE = 10
