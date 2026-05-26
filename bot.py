import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin

TOKEN = "8820626677:AAH0hUuSJ4V9BZ8oHd6pwLx7I2tUOa4dUYY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Команды: /hello, /bye, /pass, /emodji, /coin")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)
    bot.reply_to(message, "Пароль: " + password)

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, "Эмодзи: " + emodji)

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, "Монетка: " + coin)

bot.infinity_polling()