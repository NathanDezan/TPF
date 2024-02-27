import os
import telebot
from template.template import StatusTemplate
from utils.docker_fetcher import ContainerInfoFetcherFactory

BOT_TOKEN = os.getenv("BOT_TOKEN")

class TelegramBotHandler:
    def __init__(self, bot):
        self.bot = bot

    def handle_message(self, message):
        raise NotImplementedError()

class GreetingBotHandler(TelegramBotHandler):
    def handle_message(self, message):
        self.bot.reply_to(message, "Ola! Como posso te ajudar?")

class HelpBotHandler(TelegramBotHandler):
    def handle_message(self, message):
        self.bot.reply_to(message, "Comandos disponíveis:1. /start ou /hello - Saudação inicial2. /get_chat_id - Retorna o id do chat atual")

class GetChatIdBotHandler(TelegramBotHandler):
    def handle_message(self, message):
        self.bot.reply_to(message, f"{message.chat.id}")

class SendMessagesBotHandler(TelegramBotHandler):
    def handle_message(self, message):
        template = StatusTemplate()
        fetcher_docker = ContainerInfoFetcherFactory.create_fetcher()
        info_docker = fetcher_docker.fetch_info()
        test = f"|{info_docker['Nome da imagem']}\t|\t{info_docker['Status']}\t|\t|\t{info_docker['Endereço e portas utilizadas']}\t|\n"

        self.bot.send_message(message.chat.id, template.generate() + test)

class TelegramBotFactory:
    @staticmethod
    def create_bot_handler(command, bot):
        if command in ('/start'):
            return GreetingBotHandler(bot)
        elif command in ('/get_chat_id'):
            return GetChatIdBotHandler(bot)
        elif command in ('/status'):
            return SendMessagesBotHandler(bot)
        else:
            return HelpBotHandler(bot)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler()
def handle_messages(message):
    command = message.text.split()[0]
    bot_handler = TelegramBotFactory.create_bot_handler(command, bot)
    bot_handler.handle_message(message)

bot.infinity_polling()
