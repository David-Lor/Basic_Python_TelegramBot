
import requests

def send_message(token, chatid, text):
    """Send a message to a chat using a bot.
    :param token: Token of the bot to send message through
    :param chatid: Chat ID where to send the message
    :param text: Text string to send
    :return: True if message was sent
    :return: False if message could not be sent
    """
    try:
        r = requests.post("https://api.telegram.org/bot{}/sendMessage".format(token), data={
            "chat_id" : chatid,
            "text" : text
        })
        return bool(r)
    except:
        return False
