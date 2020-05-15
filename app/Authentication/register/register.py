from kivy.uix.screenmanager import Screen, ScreenManager
from app.Authentication.register.controller.RegisterController import RegisterController


class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.registerController = RegisterController()

    # Static method means that the method is related to the class and not the object of the class
    def register_user(self, username: str, password: str, email: str):
        is_registered = self.registerController.register_user(username, password, email)
        if is_registered:
            # Use parent to access other screens from py files
            self.parent.transition.direction = 'left'
            self.parent.current = 'login'
            return True
        else:
            print("Issue saving user now")
            return False
