import getpass
from hospital.user_validation import UserValidation as UV
from utils.constants import Constants
from utils.errors import UserExistsError, UserDoesntExistError, \
                PasswordOutOfConstraintsError, PasswordsDontMatchError, \
                UserNameOutOfConstraintsError, NoSuchUserTypeError, \
                AddressOutOfConstraints


class InputManager:

    @staticmethod
    def read_user_type():
        while True:
            user_type = input(f"Are you a 'doctor' or a 'patient'?\n{Constants.PROMPT} ")
            try:
                UV.validate_user_type(user_type)
                return user_type.title()
            except NoSuchUserTypeError as e:
                print(e)
            
    @staticmethod
    def read_username(sign_up=False):
        while True:
            username = input('\nUsername: ')
            try:
                UV.validate_username(username, sign_up=sign_up)
                return username
            except (UserNameOutOfConstraintsError, UserExistsError) if sign_up else UserDoesntExistError as e:
                if isinstance(e, UserDoesntExistError):
                    return None
                print(e)

    @staticmethod
    def read_password(username=None, sign_up=False):
        while True:
            password = getpass.getpass('\nPassword: ')
            if sign_up:
                try:
                    UV.validate_password(password)
                    verif_password = getpass.getpass('\nVerify password: ')
                    UV.verify_password_when_signing_up(password, verif_password)
                    salt = UV.generate_salt()
                    return UV.hash_password(password+salt), salt
                except (PasswordOutOfConstraintsError, PasswordsDontMatchError) as e:
                    print(e)
                    continue
                salt = UV.generate_salt()
            salt = UV.get_salt(username)
            return UV.hash_password(password+salt if salt else '')

    @staticmethod
    def read_doctor_type():
        return input('\nSpecialized in: ')

    @staticmethod
    def read_address():
        while True:
            address = input("\nAddress: ")
            try:
                UV.validate_patient_address(address)
                return address
            except AddressOutOfConstraints as e:
                print(e)


    @staticmethod
    def read_age():
        while True:
            age = input("\nAge: ")
            try:
                UV.validate_patient_age(age)
                return int(age)
            except ValueError as e:
                print(e)


if __name__ == '__main__':
    InputManager.read_username()