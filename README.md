# Basic Python Telegram Bot

basictelebot is a very simple Python tool to send messages via a Telegram bot. It only allows sending simple text messages to a single destination, using Python's requests native library.

## Sending messages with function

```python
from basictelebot import send_message
token = "my telegram bot token"
chatid = 123456
text = "hi there!"
send_message(token, chatid, text)
```

## Sending messages with object

```python
from basictelebot import TelegramBot
bot = TelegramBot("my telegram bot token")
chatid = 123456
text = "hi there!"
bot.send_message(chatid, text)
```

## Was the message sent successfully?

Both send_message function and class method return True if message was sent successfully, and False if any error of any type happened (including exceptions in requests module).

```python
from basictelebot import send_message
token = "my telegram bot token"
chatids = [123, 456, 789]
text = "hi there!"
for chatid in chatids:
    if send_message(token, chatid, text):
        print("Message sent to {}".format(chatid))
    else:
        print("Message could not be sent to {}".format(chatid))
```
