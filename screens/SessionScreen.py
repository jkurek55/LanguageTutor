import os.path
import time

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

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
    def on_enter(self, *args):
        self.scroll_view = self.ids['message_layout']
        self.scroll_view.add_widget(TutorMessage('elo'))
        Clock.schedule_once(self.message_appeared, 0.01)

    def message_appeared(self, *args):
        self.scroll_view.height += self.scroll_view.children[0].height + 20
        self.scroll_view.add_widget(Label(size_hint_y=None, height=20))

    def give_response(self, *args):
        self.scroll_view.add_widget(TutorMessage('odpowiadam'))
        Clock.schedule_once(self.message_appeared, 0.01)

    def send_pressed(self, message_text):
        self.scroll_view.add_widget(UserMessage(message_text))
        Clock.schedule_once(self.message_appeared, 0.01)
        #w threadingu trzeba zrobic dodawanie odpowiedzi
        Clock.schedule_once(self.give_response, 1)