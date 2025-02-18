from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


class GenericScreen(Screen):
    root = ObjectProperty()
    def __init__(self, **kwargs):
        super(GenericScreen, self).__init__(**kwargs)
        print('MainScreen init called')
    def change_screen(self, screen_name):
        self.parent.current = screen_name

