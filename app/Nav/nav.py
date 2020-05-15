from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout


class NavigationDrawer(MDNavigationDrawer):

    def __init__(self, **kwargs):
        super(NavigationDrawer, self).__init__(**kwargs)
        # self.open_progress = 0.0

    def load_dashboard(self):
        print("lets figure it out")
        self.parent.parent.parent.transition.direction = 'right'
        self.parent.parent.parent.current = 'dashboard'

    def load_food_diary(self):
        self.parent.parent.parent.transition.direction = 'right'
        self.parent.parent.parent.current = 'FoodDiary'

    def load_item_add_to_diary_screen(self):
        self.parent.parent.parent.transition.direction = 'right'
        self.parent.parent.parent.current = 'ItemAdd'


class ContentNavigationDrawer(BoxLayout):
    def __init__(self, **kwargs):
        super(ContentNavigationDrawer, self).__init__(**kwargs)


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):

    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
        print("instance_item, need to figure pout how to set menu item as active -> ", instance_item.text)
        print("current screen",  self.parent.parent.parent.parent.parent.parent.current)
        # instance_item.text_color = self.theme_cls.primary_color
        # # Set the color of the icon and text for the menu item.
        # for item in self.children:
        #     if item.text_color == self.theme_cls.primary_color:
        #         item.text_color = self.theme_cls.text_color
        #         break
        # instance_item.text_color = self.theme_cls.primary_color
