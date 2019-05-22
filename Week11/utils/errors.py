class PasswordsDontMatchError(Exception):
    def __init__(self, message):
        super().__init__(message)


class UserExistsError(Exception):
    def __init__(self, message):
        super().__init__(message)

class UserDoesntExistError(Exception):
    def __init__(self, message):
        super().__init__(message)


class UserNameOutOfConstraintsError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PasswordOutOfConstraintsError(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoSuchUserTypeError(Exception):
    def __init__(self, message):
        super().__init__(message)


class AddressOutOfConstraints(Exception):
    def __init__(self, message):
        super().__init__(message)