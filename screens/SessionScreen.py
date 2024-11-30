import os.path

from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from screens.GenericScreen import *
Builder.load_file(os.path.join('screens', 'SessionScreen.kv'))

class MessageScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(MessageScrollView, self).__init__(**kwargs)

class Message(Label):
    def __init__(self, **kwargs):
        super(Message, self).__init__(**kwargs)
class SessionScreen(GenericScreen):
    def __init__(self, **kwargs):
        super(SessionScreen, self).__init__(**kwargs)
        print('MainScreen init called')
