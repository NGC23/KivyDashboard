from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from app.Nutrition.controller.addItemController import AddItemController


class ItemAdd(Screen):

    def __init__(self, **kwargs):
        super(ItemAdd, self).__init__(**kwargs)
        self.controller = AddItemController()

    def add(self):
        self.controller.add()
