class Message:

    def __init__(self, user_id, message_content, message_date) -> None:
        self.user_id = user_id
        self.message_content = message_content
        self.message_date = message_date

    def createMessage(self, user_id, message_content, message_date):
        # this def send the data from sender or recevier to the server

        with open('test_message.txt', 'w') as file:
            file.write(f'{user_id}: {message_date}\n {message_content}\n')

    def showMessage():
        # this def retrive the message from the server and show it the screen
        pass
