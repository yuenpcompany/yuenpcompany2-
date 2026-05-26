import telebot
from bot_logic import gen_pass, flip_coin
import random

TOKEN = "8820626677:AAH0hUuSJ4V9BZ8oHd6pwLx7I2tUOa4dUYY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "привет! /help")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "/pass - пароль\n/coin - монетка\n/dice - кубик\n/8ball - шар\n/random - число\n/ping - пинг\n/roll - д20\n/choose - выбор\n/rock - камень\n/slot - слот\n/hack - взлом\n/fact - факт\n/russian - рулетка")

@bot.message_handler(commands=['pass'])
def passw(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['coin'])
def coin(message):
    bot.reply_to(message, flip_coin())

@bot.message_handler(commands=['dice'])
def dice(message):
    bot.send_dice(message.chat.id, "🎲")

@bot.message_handler(commands=['8ball'])
def eight_ball(message):
    answers = ["да", "нет", "возможно", "точно да", "точно нет"]
    bot.reply_to(message, random.choice(answers))

@bot.message_handler(commands=['random'])
def rand(message):
    bot.reply_to(message, str(random.randint(1, 100)))

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.reply_to(message, "понг!")

@bot.message_handler(commands=['roll'])
def roll(message):
    bot.reply_to(message, str(random.randint(1, 20)))

@bot.message_handler(commands=['choose'])
def choose(message):
    opts = message.text.replace("/choose", "").strip().split()
    if len(opts) >= 2:
        bot.reply_to(message, random.choice(opts))
    else:
        bot.reply_to(message, "пример: /choose да нет")

@bot.message_handler(commands=['rock'])
def rock(message):
    p = message.text.replace("/rock", "").strip().lower()
    b = random.choice(["камень", "ножницы", "бумага"])
    if p in ["камень", "ножницы", "бумага"]:
        if p == b:
            bot.reply_to(message, "ничья - " + b)
        elif (p == "камень" and b == "ножницы") or (p == "ножницы" and b == "бумага") or (p == "бумага" and b == "камень"):
            bot.reply_to(message, "ты выиграл! бот: " + b)
        else:
            bot.reply_to(message, "бот выиграл! бот: " + b)
    else:
        bot.reply_to(message, "пиши: камень, ножницы или бумага")

@bot.message_handler(commands=['slot'])
def slot(message):
    e = ["🍒", "🍊", "🍋", "7️⃣", "💎", "⭐"]
    a = random.choice(e)
    b = random.choice(e)
    c = random.choice(e)
    if a == b == c:
        r = "ДЖЕКПОТ!"
    elif a == b or b == c or a == c:
        r = "выигрыш"
    else:
        r = "проигрыш"
    bot.reply_to(message, a + " " + b + " " + c + " - " + r)

@bot.message_handler(commands=['hack'])
def hack(message):
    t = message.text.replace("/hack", "").strip()
    if t:
        bot.reply_to(message, "взлом " + t + "...\n3...\n2...\n1...\n💀 " + t + " взломан!")
    else:
        bot.reply_to(message, "кого? пример: /hack петя")

@bot.message_handler(commands=['fact'])
def fact(message):
    facts = [
        "у осьминога 3 сердца",
        "бананы - это ягоды",
        "страусы не прячут голову",
        "крокодилы не высовывают язык",
        "пчелы спят в цветах",
        "кошки спят 70% жизни",
        "у улитки 25000 зубов",
        "слоны не умеют прыгать"
    ]
    bot.reply_to(message, random.choice(facts))

@bot.message_handler(commands=['russian'])
def russian(message):
    chamber = random.randint(1, 6)
    if chamber == 1:
        bot.reply_to(message, "💀 ты проиграл")
    else:
        bot.reply_to(message, "🍀 повезло! патрон был в " + str(chamber))

bot.infinity_polling()
