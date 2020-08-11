import telebot
from datetime import datetime


class GreeterBot:
    def __init__(self):
        self.bot = telebot.TeleBot("816056658:AAF_e8ZWZMBF_05Eb-2cDnxPzlFiX-32i8g")

        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            self.bot.send_message(message.chat.id, f'Привет, сейчас {datetime.now()}')
