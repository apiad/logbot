from telegram.ext import Updater, CommandHandler


class Bot:
    def __init__(self, token):
        self.token = token
        self.updater = Updater(self.token)
        self.dispatcher = self.updater.dispatcher

        # register methods
        self.dispatcher.add_handler(CommandHandler('start', self._start))

    def _start(self, bot, update):
        return bot.send_message(update.message.chat_id, "I'm ready to start.")

    def run(self):
        self.updater.start_polling()
        self.updater.idle()
