import telebot

bot = telebot.TeleBot('6165937863:AAG0ZIDGsBVLxXVaGnJTebM4odMacTPg_-I',parse_node=None)


@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.chat.id, 'የመመዝገቢያ ቦት ላይ እንኳን በደህና መጡ!')
    bot.send_message(message.chat.id, 'ስምዎን እባክዎ ያስገቡ:', reply_markup=ReplyKeyboardMarkup(
        keyboard=[['ስም']], resize_keyboard=True))


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() == 'ስም':
        bot.send_message(message.chat.id, 'ስምዎን እባክዎ ያስገቡ:', reply_markup=ReplyKeyboardMarkup(
            keyboard=[['ስም']], resize_keyboard=True))
    else:
        bot.send_message(message.chat.id, 'ስምዎን በመጀመሪያ ስም መጨረሻ ስም ቅርጸት ያስገቡ.')


bot.polling()