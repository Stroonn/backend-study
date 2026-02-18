class UserError(Exception):
    """Base class for user-related errors"""
    pass

class EmptyUsernameError(UserError):
    pass

class EmptyEmailError(UserError):
    pass

class InvalidEmailError(UserError):
    pass

class UserDuplicateError(UserError):
    pass