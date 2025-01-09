import os.path
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
import json
from ai.LanguageTutor import LanguageTutor
from screens.GenericScreen import *
Builder.load_file(os.path.join('screens', 'SessionScreen.kv'))

class MessageScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(MessageScrollView, self).__init__(**kwargs)



class UserMessage(BoxLayout):
    message_text = StringProperty()
    def __init__(self, message_text, **kwargs):
        super(UserMessage, self).__init__(**kwargs)
        self.message_text = message_text

class TutorMessage(BoxLayout):
    message_text = StringProperty()
    def __init__(self, message_text, **kwargs):
        super(TutorMessage, self).__init__(**kwargs)
        self.message_text = message_text


class SessionScreen(GenericScreen):
    def __init__(self, **kwargs):
        super(SessionScreen, self).__init__(**kwargs)
        print('MainScreen init called')

    def old_messages_appeared(self, *args):
        cumulated_height = 0
        for child in self.scroll_view.children:
            cumulated_height += child.height

        self.scroll_view.height += cumulated_height

    def view_old_messages(self):
        for message in self.root.messages:
            if message['role'] == 'user' and message['content'] != '':
                self.scroll_view.add_widget(UserMessage(message['content']))
                self.scroll_view.add_widget(Label(size_hint_y=None, height=20))

            elif message['role'] == 'assistant' and message['content'] != '':
                self.scroll_view.add_widget(TutorMessage(message['content']))
                self.scroll_view.add_widget(Label(size_hint_y=None, height=20))

        Clock.schedule_once(self.old_messages_appeared, 0.01)


    def on_enter(self, *args):
        self.scroll_view = self.ids['message_layout']
        #self.language_tutor = LanguageTutor(system_query)
        self.language_tutor = LanguageTutor(self.root.messages)

        tutor_greeting = ''

        self.view_old_messages()

        self.scroll_view.add_widget(TutorMessage(self.language_tutor.generate_answer(tutor_greeting)))
        #self.scroll_view.add_widget(TutorMessage(tutor_greeting))
        Clock.schedule_once(self.message_appeared, 0.01)

    def message_appeared(self, *args):
        self.scroll_view.height += self.scroll_view.children[0].height + 20
        self.scroll_view.add_widget(Label(size_hint_y=None, height=20))

    def show_response(self, response):
        self.scroll_view.add_widget(TutorMessage(response))
        Clock.schedule_once(self.message_appeared, 0.01)

    def generate_response(self, user_prompt, *args):
        response = self.language_tutor.generate_answer(user_prompt)
        self.show_response(response)


    def send_pressed(self, message_text):
        self.scroll_view.add_widget(UserMessage(message_text))
        Clock.schedule_once(self.message_appeared, 0.01)
        Clock.schedule_once(partial(self.generate_response, message_text), 1)

    def save_and_exit(self):
        with open('session.json', 'w', encoding='utf-8') as f:
            json.dump(self.language_tutor.messages, f, ensure_ascii=False, indent=4)
        App.get_running_app().stop()