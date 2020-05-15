from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from app.Authentication.login.login import LoginScreen
from app.Authentication.register.register import RegisterScreen
from app.Dashboard.dashboard import Dashboard
from app.Nutrition.itemAdd import ItemAdd
from app.Nutrition.foodDiary import FoodDiary
from bin import PrepApplicationInstall
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', False)


class MainAppScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        return ScreenManagement()


if __name__ == "__main__":
    # App install script - this will only be initiated once in the applications lifecycle
    PrepApplicationInstall()
    # Main app to run
    MainApp().run()

