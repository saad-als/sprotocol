from backend.messages.message import Message
import datetime


class Sender:

    def __init__(self, name, user_id) -> None:
        self.name = name
        self.user_id = user_id

    def sendMessage(self, name, user_id, text):

        message = Message(user_id=self.user_id, message_content=text,
                          message_date=datetime.datetime.now())
        message.createMessage(user_id, text, datetime.datetime.now())
