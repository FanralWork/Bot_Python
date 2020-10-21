import telebot
bot = telebot.TeleBot('1345627871:AAEo4OD-AhQCDWS77DUo_-P7VUz2ZsuXDuo')

@bot.message_handler(commands=["start"])
def heandle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("/start", "/stop")
    user_markup.row("/help", "/info")
    user_markup.row("/games", "/programs")
    bot.send_message(message.chat.id, """Привет я Хоттабыч. Я могу помочь тебе купить игры со скидкой,
чтобы узнать мои команды введи /help""", reply_markup=user_markup)
    bot.send_photo(message.chat.id, 'http://memok.net/uploads/2015/10/24/562c19b19826a.jpg', reply_markup=user_markup)
#Приветствие#

@bot.message_handler(commands=["stop"])
def heandle_stop(message):
    remove_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,  "Мы закончили?... Ладно...(", reply_markup=remove_markup)

@bot.message_handler(commands=["info"])
def handle_text(message):
    bot.send_message(message.chat.id, """Версия бота: 1.3""")
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
Garry's Mod - 249 рублей""", reply_markup = markup)

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Купить", callback_data='Link_Buy_Garrys_Mod')
    item1 = types.InlineKeyboardButton("Перейти в магазин", callback_data='Link_Garrys_Mod')

    markup.add(item1, item2)
    #Игры#

@bot.message_handler(commands=["programs"])
def handle_text(message):
    bot.send_message(message.chat.id, """Все программы:
GameGuru - 699 рублей - https://store.steampowered.com/app/266310/GameGuru""")
#Программы#

@bot.message_handler(content_types=["text"])
def handle_text(message):
        if message.text == "я тоже не знаю" or message.text == "Я тоже не знаю":
            bot.send_message(message.chat.id, "Приятно познакомится, собрат по разуму")
        else: bot.send_message(message.chat.id, "Я не знаю такой команды.")
#Ответ на бред#

bot.polling(none_stop=True, interval=0)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '123':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '567':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
