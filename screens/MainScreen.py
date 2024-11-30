import os.path

from kivy.lang import Builder
from screens.GenericScreen import *

Builder.load_file(os.path.join('screens', 'MainScreen.kv'))

class MainScreen(GenericScreen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        print('MainScreen init called')
