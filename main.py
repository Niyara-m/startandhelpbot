import telebot, buttons

bot = telebot.TeleBot('6485732580:AAHHPdQFIgUyuRhDWRTC4Xixk14SsalNeL4')

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.from_user.id, f'{message.from_user.first_name}! Добро пожаловать!',reply_markup=buttons.help_button())
    bot.register_next_step_handler(message, help_message)

@bot.message_handler(commands=['help'])

def help_message(message):
    bot.send_message(message.from_user.id, '/start - команда старт нужна для начала работы с ботом! /help - это команда покажет вам все возможные инструкции', reply_markup=telebot.types.ReplyKeyboardRemove())

bot.polling(non_stop=True)