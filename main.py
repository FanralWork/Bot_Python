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

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))    

bot.polling(none_stop=True, interval=0)
