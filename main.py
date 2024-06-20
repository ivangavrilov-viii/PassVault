from telebot.types import Message, CallbackQuery
from init.messages import *
from decouple import config
from loguru import logger
import telebot


bot = telebot.TeleBot(config('bot_token'))
admin_list = [int(config('admin_id'))]


@bot.message_handler(content_types=['text'])
def start(message: Message) -> None:
    """ CALLING AND PROCESSING BASIC BOT COMMANDS """

    user_id = message.chat.id

    if message.text == '/start':
        bot.send_message(user_id, start_bot_message(message))
        bot.send_message(user_id, function_list(user_id))



if __name__ == '__main__':
    logger.add('debug_log.log', level='DEBUG', format='{time} | {level} | {message}', encoding='utf-8')
    bot.polling(none_stop=True, interval=0)
