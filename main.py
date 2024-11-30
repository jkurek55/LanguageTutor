import os

import kivy
from kivy import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

from screens.MainScreen import *

Builder.load_file('MainScreenManager.kv')
class MainScreenManager(Widget):
    def __init__(self, **kwargs):
        super(MainScreenManager, self).__init__(**kwargs)
        print('MainScreen init called')


class LanguageTutorApp(App):
    def build(self):
        return MainScreenManager()


if __name__ == '__main__':
    LanguageTutorApp().run()