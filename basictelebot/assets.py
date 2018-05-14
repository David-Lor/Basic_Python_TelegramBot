
from .helpers import send_message

class TelegramBot(object):
    def __init__(self, token):
        """
        :param token: Token of the bot to send the messages through
        """
        self.token = token
    
    def send_message(self, chatid, text):
        """Send a message to a chat using the bot.
        :param chatid: Chat ID where to send the message
        :param text: Text string to send
        :return: True if message was sent
        :return: False if message could not be sent
        """
        return send_message(self.token, chatid, text)
