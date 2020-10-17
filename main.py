import telebot
bot = telebot.TeleBot('1345627871:AAEo4OD-AhQCDWS77DUo_-P7VUz2ZsuXDuo')

@bot.message_handler(commands=["start"])
def handle_text(message):
    bot.send_message(message.chat.id, """Привет я Хоттабыч. Я могу помочь тебе купить игры со скидкой,
чтобы узнать мои команды введи /help""")
#Приветствие#

@bot.message_handler(commands=["info"])
def handle_text(message):
    bot.send_message(message.chat.id, """Версия бота: 1.2""")
#информация#

@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, """Мои команды:
/games - Купить игры
/programs - купить программы""")
#Все команды#

@bot.message_handler(commands=["games"])
def handle_text(message):
    bot.send_message(message.chat.id, """Все игры:
Garry's Mod - 249 рублей - https://store.steampowered.com/app/4000/Garrys_Mod""")
#Игры#

@bot.message_handler(commands=["programs"])
def handle_text(message):
    bot.send_message(message.chat.id, """Все программы:
GameGuru - 699 рублей - https://store.steampowered.com/app/266310/GameGuru""")
#Программы#

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, "Я не знаю такой команды.")
#Ответ на бред#

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "я тоже не знаю" or message.text == "Я тоже не знаю":
        bot.send_message(message.chat.id, "Приятно познакомится, собрат по разуму")
#пасхалка#

bot.polling(none_stop=True, interval=0)
