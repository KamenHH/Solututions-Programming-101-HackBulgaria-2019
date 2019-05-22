from controller.input_manager import InputManager


class MainController:

    @classmethod
    def sign_up(cls):
        while True:
            username = InputManager.read_username()
            password = InputManager.read_password()
            if InputManager.verify_password_when_signing_in(password):
                return username, password



    @classmethod
    def sign_in(cls):
        pass
        # cls._validate_password(password)
        # cls._validate_password(second_password)

        # hashed_pass1 = cls._hash_password(password)
        # hassed_pass2 = cls._hash_password(second_password)
        # cls._do_passwords_match(hashed_pass1, hassed_pass2)

        # if User.find(username, password):
        #     raise UserAlreadyExistsError

        # return User.create_new_user(username, hashed_pass1)

    @classmethod
    def show_members(cls, current_user):
        pass
        # if current_user.is_doctor:
        #     return cls.show_patients(current_user)
        #     #  [Patient('Roza'), Patient('Mimi')]
        # else:
        #     return cls.show_doctors(current_user)