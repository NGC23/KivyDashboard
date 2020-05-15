from app.Authentication.login.repositories.loginRepository import LoginRepository
from app.Authentication.models import User


class LoginController(object):

    def __init__(self):
        super(LoginController, self).__init__()
        self.login_repository = LoginRepository()

    def login_user(self, username: str, password: str) -> User:
        try:
            current_user = self.login_repository.login_user(username, password)
            print("we have a user", current_user)
        except Exception as exception:
            raise Exception("There is an issue signing in user", str(exception))

        return current_user
