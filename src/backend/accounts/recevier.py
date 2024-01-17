from backend.messages.message import Message
import datetime


class Recevier:

    def __init__(self, name, user_id) -> None:
        self.name = name
        self.user_id = user_id

    def sendMessage(self, name, user_id, text):

        message = Message(user_id=self.user_id, message_content=text,
                          message_date=datetime.datetime.now())

        return message
