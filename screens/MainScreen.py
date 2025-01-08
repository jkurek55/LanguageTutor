import json
import os

from kivy.lang import Builder
from screens.GenericScreen import *

Builder.load_file(os.path.join('screens', 'MainScreen.kv'))

class MainScreen(GenericScreen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        print('MainScreen init called')
    def load_session(self):
        with open('session.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        self.root.load_settings(data)
        self.root.current = 'session_screen'