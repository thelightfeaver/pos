from src.models.user import User


def login(username, password):
    try:
        user = User.get(User.username == username, User.password == password)
        return user
    except User.DoesNotExist:
        return None
