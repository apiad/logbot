import time
import json

from telegram.ext import Updater, CommandHandler
from threading import Thread
from queue import Queue
from flask import Flask, jsonify, request


class Bot:
    def __init__(self, token):
        self.token = token
        self.updater = Updater(self.token)
        self.dispatcher = self.updater.dispatcher
        self.bot = self.updater.bot
        self.queue = MessageQueue()
        self.started = False
        self.chat_id = None

        # register methods
        self.dispatcher.add_handler(CommandHandler('start', self._start))

    def _start(self, bot, update):
        if self.started:
            bot.send_message(update.message.chat_id, "Sorry, already talking to someone else.")
            return

        self.started = True
        self.queue.started = True
        self.chat_id = update.message.chat_id

        return bot.send_message(update.message.chat_id, "I'm ready to start.")

    def run(self):
        self.queue.start()
        self.updater.start_polling()

        try:
            while True:
                msg = self.queue.get()
                self.bot.send_message(self.chat_id, str(msg))

        except KeyboardInterrupt:
            return


class MessageQueue(Thread):
    def __init__(self):
        super().__init__(name="message-queue", daemon=True)
        self.app = Flask("message-queue")
        self.queue = Queue()
        self.started = False

        @self.app.route("/", methods=['POST'])
        def post():
            if not self.started:
                return "Not /start command given yet", 404

            data = request.get_json(force=True)
            self.queue.put(data)
            return jsonify(data)

    def get(self):
        return self.queue.get()

    def run(self):
        print("Running the message queue")
        self.app.run('localhost', 6778)
