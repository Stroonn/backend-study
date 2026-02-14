from app.models.user import User

class UserService:
    def create_user(self, name:str, email:str) -> User:
        return User(name, email)