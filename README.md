import telebot
import time
from telebot.handler_backends import ContinueHandling
import random, os

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8462521511:AAGJ5oTBHkzIZTiwr1qlG2CRPidgRwLEgrs")


def calc(a, b):
    return int(a) + int(b)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет,я Экобот!")



@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")


@bot.message_handler(commands=['calc'])
def send_hello(message):
    try:
        ab = message.text.split()
        bc = message.text.split(',')
        print(ab, bc)
        bot.reply_to(message, calc(ab[1], ab[2]))

    except:
        bot.reply_to(message, 'введите /calc число а и число в через пробел')


@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, 'колобок повесился')


@bot.message_handler(commands=['heh'])
def send_heh(message):
    time.sleep(3)
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=['mem'])
def send_image(message):
    img = random.choice(os.listdir('images'))
    with open(f'images/{img}', 'rb') as f:
        bot.send_photo(message, f)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.reply_to(message, message.text)
    return ContinueHandling()


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 2 and args[1].isdigit() and args[2].isdigit():
        for i in range(int(args[2])):
            sec = int(args[1])
            bot.reply_to(message, 'beep!')
            time.sleep(sec)

    else:
        bot.reply_to(message, 'Usage: /set <seconds> <times>')


print('старт')
bot.polling()
