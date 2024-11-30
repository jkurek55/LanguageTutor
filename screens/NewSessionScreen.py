import os.path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from screens.GenericScreen import *

Builder.load_file(os.path.join('screens', 'NewSessionScreen.kv'))

class NewSessionScreen(GenericScreen):
    def __init__(self, **kwargs):
        super(NewSessionScreen, self).__init__(**kwargs)
        print('MainScreen init called')