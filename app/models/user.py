from dataclasses import dataclass
from app.errors.user_errors import EmptyUsernameError, EmptyEmailError

@dataclass
class User:

    name : str
    email : str

    def __post_init__(self):
        if not self.name:
            raise EmptyUsernameError("Name cannot be empty")
        if not self.email:
            raise EmptyEmailError("Email cannot be empty")