import time
import json
import random
import asyncio

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
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
        self.chat_ids = dict()
        self.updater = Updater(self.token)
        self.dispatcher = self.updater.dispatcher

        # register bot methods
        self.bot = self.updater.bot
        self.dispatcher.add_handler(CommandHandler('start', self._start))
        self.dispatcher.add_handler(CallbackQueryHandler(self._callback))

        # register bot endpoints
        self.app = Sanic("message-queue")
        self.app.add_route(self._post, "/", methods=['POST'])

        # callback ids
        self.callbacks = {}

    async def _post(self, request):
        data = request.json

        token = data['token']
        msg = data['msg']
        user = self.chat_ids[token]
        actions = data.get('actions', [])
        reply_token = random_key(12)

        if actions:
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton(s, callback_data=reply_token + "/" + s) for s in actions
            ]])
        else:
            reply_markup = None

        message = self.bot.send_message(user, msg, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

        if not actions:
            return json(dict(msg=msg))

        while not reply_token in self.callbacks:
            await asyncio.sleep(1)

        response = self.callbacks.pop(reply_token)
        return json(dict(msg=msg, response=response))

    def _callback(self, bot, update):
        token, response = update.callback_query.data.split("/")
        update.callback_query.answer()
        update.callback_query.edit_message_reply_markup(reply_markup=None)
        self.callbacks[token] = response

    def _start(self, bot, update):
        msg_token = random_key(12)
        self.chat_ids[msg_token] = update.message.chat_id
        update.message.reply_markdown("This is your custom message token:\n*{0}*".format(msg_token))

    def run(self, host='localhost', port=6778):
        self.updater.start_polling()
        self.app.run(host, port)
