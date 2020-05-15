from app.Authentication.register.repositories.registerRepository import RegisterRepository


class RegisterController(object):

    def __init__(self):
        print("init called in controller")
        super(RegisterController, self).__init__()
        self.registerRepo = RegisterRepository()

    def register_user(self, username: str, password: str, email: str) -> bool:
        register_user: bool = self.registerRepo.register_user(username, password, email)

        if register_user:
            print("User has been registered, let us redirect him to the dashboard")
            return True

        # Error registering the user
        return False


