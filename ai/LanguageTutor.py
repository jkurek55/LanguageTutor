import os.path
f = open(os.path.join('ai', 'APIKey.txt'), "r")
APIKey = f.readlines()[0]

import openai
from openai import OpenAI
openai.api_key = APIKey



class LanguageTutor:
    client = openai.OpenAI(api_key=APIKey)
    message_limit = 50

    def __init__(self, historic_messages):
        self.messages: list = historic_messages

    def downsize_context(self):
        while len(self.messages) > self.message_limit:
            if self.messages[1]['role'] in ['user', 'assistant']:
                self.messages.pop(1)

    def generate_answer(self, user_query):
        self.messages.append({"role": "user", "content": user_query})

        tutor_answer = self.client.chat.completions.create(
            messages=self.messages,
            model="gpt-4o-mini",
            temperature=0
        ).choices[0].message.content.strip()

        self.messages.append({"role": "assistant", "content": tutor_answer})
        self.downsize_context()

        return tutor_answer

    def get_history(self):
        return self.messages

    def get_context(self):
        return self.context

