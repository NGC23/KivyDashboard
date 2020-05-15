from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from datetime import date


class FoodDiary(Screen):
    dialog = None
    protein = StringProperty('1234')
    calories = StringProperty('1234')
    fats = StringProperty('1234')
    current_date = date.today()
    date_diary = StringProperty(current_date.strftime("%d/%m/%Y"))

    def __init__(self, **kwargs):
        super(FoodDiary, self).__init__(**kwargs)

    # Here i can set on_release methods for each button and they will refer to functions
    # In the current screen context witch would be ItemAdd
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL"
                    ),
                    MDFlatButton(
                        text="DISCARD"
                    ),
                ],
            )
        self.dialog.open()

    def load_add_item_screen(self):
        self.parent.current = 'ItemAdd'
