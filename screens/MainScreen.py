import os.path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file(os.path.join('screens', 'MainScreen.kv'))

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        print('MainScreen init called')