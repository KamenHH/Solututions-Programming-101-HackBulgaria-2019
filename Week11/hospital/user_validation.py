import hashlib
import secrets
import string
from utils.constants import Constants
from database_layer.db_manager import DBManager
from utils.errors import UserExistsError, UserDoesntExistError, \
                PasswordOutOfConstraintsError, PasswordsDontMatchError, \
                UserNameOutOfConstraintsError, NoSuchUserTypeError, \
                AddressOutOfConstraints


class UserValidation:

    @staticmethod
    def validate_user_type(user_type):
        if user_type.title() not in Constants.USER_TYPES:
            raise NoSuchUserTypeError('Error, no such user type!')

    @staticmethod
    def validate_username(username, sign_up=False):
        if len(username) > Constants.USERNAME_MAX_SIZE or len(username) < Constants.USERNAME_MIN_SIZE:
            raise UserNameOutOfConstraintsError('Error, username must be between ' \
                                                f'{Constants.USERNAME_MIN_SIZE} and {Constants.USERNAME_MAX_SIZE} characters! Please, try again!')
        
        if DBManager.check_if_user_exists(username) and sign_up:
            raise UserExistsError('Error, user with the provided username already exists!')
        elif not DBManager.check_if_user_exists(username) and not sign_up:
            raise UserDoesntExistError('Error, a user with the provided username doesn\'t exist!')

    @staticmethod
    def validate_password(password):
        if len(password) > Constants.PASSWORD_MAX_SIZE or len(password) < Constants.PASSWORD_MIN_SIZE:
            raise PasswordOutOfConstraintsError(f'Error, password must be between {Constants.PASSWORD_MIN_SIZE} and {Constants.PASSWORD_MAX_SIZE} characters!' \
                                                'Please, try again!')


    @staticmethod
    def validate_patient_address(address):
        if len(address) > Constants.ADDRESS_MAX_SIZE:
            raise AddressOutOfConstraints(f'Error, address must be less than {Constants.ADDRESS_MAX_SIZE} characters! Please, try again!')


    @staticmethod
    def validate_patient_age(age):
        try:
            int(age)
        except ValueError:
            raise ValueError('Error, agea must be a valid positive integer!')
        if int(age) < 0 or int(age) > 100:
            raise ValueError('Error, agea must be a valid positive integer!')

    @staticmethod
    def verify_password_when_signing_up(password, verif_password):
        if verif_password != password or \
            UserValidation.hash_password(verif_password) != UserValidation.hash_password(password):
            raise PasswordsDontMatchError('Error, provided passwords don\'t match!')

    @staticmethod
    def hash_password(password):
        return hashlib.md5(password.encode()).hexdigest()

    @staticmethod
    def generate_salt():
        salt = ''
        for ch in range(Constants.SALT_SIZE):
            salt += secrets.choice(string.ascii_letters+string.digits +
                                   Constants.SYMBOLS_FOR_SALT)
        return salt

    @staticmethod
    def get_salt(username):
        return DBManager.get_salt(username)
