import time
import json
import random

from telegram.ext import Updater, CommandHandler
from telegram import ParseMode
from threading import Thread
from queue import Queue
from sanic import Sanic
from sanic.response import json


def random_key(size):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = symbols + symbols.lower()
    symbols = symbols + "0123456789"

    return "".join(random.sample(symbols, size))


class Bot:
    def __init__(self, token):
        self.token = token
        self.updater = Updater(self.token)
        self.dispatcher = self.updater.dispatcher
        self.bot = self.updater.bot
        self.queue = MessageQueue()
        self.chat_ids = dict()
        self.app = Sanic("message-queue")

        @self.app.route("/", methods=['POST'])
        async def post(request):
            data = request.get_json(force=True)

            print(data)

            return json(data)

        # register methods
        self.dispatcher.add_handler(CommandHandler('start', self._start))

    def _start(self, bot, update):
        msg_token = random_key(12)
        self.chat_ids[msg_token] = update.message.chat_id

        return update.message.reply_markdown("This is your custom message token:\n*{0}*".format(msg_token))

    def run(self):
        self.updater.start_polling()
        self.app.run('localhost', 6778)
