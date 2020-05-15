from kivy.uix.screenmanager import Screen
from app.Authentication.login.controller.LoginController import LoginController
from app.Authentication.models.User import User


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.login_controller = LoginController()

    def login_user(self, username: str, password: str):
        try:
            current_user = self.login_controller.login_user(username, password)
            print("login is fine")
            self.parent.current = 'dashboard'
        except RuntimeError as error:
            print("error", error)
