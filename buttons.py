from telebot import types

def help_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    help = types.KeyboardButton('Помощь')

    kb.add(help)
    return kb