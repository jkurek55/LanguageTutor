import os

import kivy
from kivy import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget

from screens.MainScreen import *
from screens.NewSessionScreen import *
from screens.SessionScreen import *

from config.agent_system_settings import *

Builder.load_file('MainScreenManager.kv')




class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MainScreenManager, self).__init__(**kwargs)
        self.messages = []
        print('MainScreen init called')

    def set_settings_for_session(self, language, level, appearance):
        system_prompt = create_agent_system(language, level)
        #f'Jesteś miłym konsultantem. {language}. {level}. {appearance}'
        self.messages = [{"role": "system", "content": system_prompt}]


    def load_settings(self, messages):
        '''tutaj sa wgrywane messages z pliku'''
        self.messages = messages



class LanguageTutorApp(App):
    def build(self):
        return MainScreenManager()


if __name__ == '__main__':
    LanguageTutorApp().run()