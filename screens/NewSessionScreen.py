import os.path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from screens.GenericScreen import *

Builder.load_file(os.path.join('screens', 'NewSessionScreen.kv'))

class NewSessionScreen(GenericScreen):
    def __init__(self, **kwargs):
        super(NewSessionScreen, self).__init__(**kwargs)
        print('MainScreen init called')

    def start_new_session(self):
        '''ta funkcja ma brac ze spinnerow jezyk i inne parametry i pozniej tworzyc nowa sesje
        na ich podstawie'''

        language = self.ids['language_spinner'].text
        level = self.ids['level_spinner'].text
        appearance = self.ids['appearance_spinner'].text

        self.root.set_settings_for_session(language, level, appearance)
        self.root.current = 'session_screen'
        # wymyslic gdzie new session screen ma byc wywolywany
