import telebot
from telebot import types
basket = 0

bot = telebot.TeleBot('1345627871:AAEo4OD-AhQCDWS77DUo_-P7VUz2ZsuXDuo')

@bot.message_handler(commands=["start"])
def heandle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("/start", "/stop")
    user_markup.row("/help", "/info")
    user_markup.row("/games", "/basket")
    bot.send_message(message.chat.id, """Привет я Хоттабыч. Я могу помочь тебе купить игры со скидкой,
чтобы узнать мои команды введи /help""", reply_markup=user_markup)
    bot.send_photo(message.chat.id, 'http://memok.net/uploads/2015/10/24/562c19b19826a.jpg', reply_markup=user_markup)

# Приветствие#

@bot.message_handler(commands=["basket"])
def heandle_stop(message):
    remove_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, basket, reply_markup=remove_markup)

@bot.message_handler(commands=["stop"])
def heandle_stop(message):
    remove_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Мы закончили?... Ладно...(", reply_markup=remove_markup)


@bot.message_handler(commands=["info"])
def handle_text(message):
    bot.send_message(message.chat.id, """Версия бота: 1.3""")


# информация#

@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, """Мои команды:
/games - Купить игры
/start - Начать работу
/stop - Закончить работу с ботом
/info - Информация о версии бота""")
#/programs - купить программы#



# Все команды#

@bot.message_handler(commands=["games"])
def handle_text(message):
    bot.send_message(message.chat.id, text="Все игры:")

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Купить", callback_data='Link_Buy_GTA_5')
    item2 = types.InlineKeyboardButton("Перейти в магазин", callback_data='Link_GTA_5')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, text="GTA 5 - 645 рублей", reply_markup=markup)
    #GTA 5#

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Купить", callback_data='Link_Buy_Fallout_76')
    item2 = types.InlineKeyboardButton("Перейти в магазин", callback_data='Link_GTA_5')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, text="Fallout 76 - 479 рублей", reply_markup=markup)
    #Fallout 76#

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Купить", callback_data='Link_Buy_PUBG')
    item2 = types.InlineKeyboardButton("Перейти в магазин", callback_data='Link_GTA_5')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, text="PUBG - 379 рублей", reply_markup=markup)
    #PUBG#

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Перейти в магазин", callback_data='Link_GTA_5')
    markup.add(item1)
    bot.send_message(message.chat.id, text="Чтобы увидеть ещё игры прейди на сайт.", reply_markup=markup)
    #Переход на сайт#


# Игры#

# @bot.message_handler(commands=["programs"])
# def handle_text(message):
#     bot.send_message(message.chat.id,
#                      "Все программы: \n GameGuru - 699 рублей - https://store.steampowered.com/app/266310/GameGuru")
#
#
# # Программы#

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "я тоже не знаю" or message.text == "Я тоже не знаю":
        bot.send_message(message.chat.id, "Приятно познакомится, собрат по разуму")
    else:
        bot.send_message(message.chat.id, "Я не знаю такой команды.")


# Ответ на бред#

@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    try:
        if call.message:
            if call.data == "Link_Buy_GTA_5":
                bot.send_message(call.message.chat.id,
                                 "https://zaka-zaka.com/game/grand-theft-auto-v-criminal-enterprise-starter-pack/?agent=#1965376")
            elif call.data == 'Link_GTA_5':
                bot.send_message(call.message.chat.id, "https://zaka-zaka.com/?agent=#1965376")

            elif call.data == "Link_Buy_Fallout_76":
                bot.send_message(call.message.chat.id,
                                 "https://zaka-zaka.com/game/fallout-76/?agent=#1965376")
            elif call.data == "Link_Buy_PUBG":
                bot.send_message(call.message.chat.id,
                                 "https://zaka-zaka.com/game/playerunknowns-battlegrounds/?agent=#1965376")
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Чтобы купить игру прейди на сайт.",
                                      reply_markup=None)
    except Exception as e:
        print(repr(e))
# Обработка инлайн кнопок#

bot.polling(none_stop=True, interval=0)
