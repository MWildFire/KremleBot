import telebot
from telebot import types
import time

bot = telebot.TeleBot ('')

firstNum = 0
secondNum = 0
point = ''
result = 0


@bot.message_handler(content_types = ['text'])
def start (message):
    global firstNum
    if message.text == '/start':
        bot.send_sticker(message.from_user.id, 'CAADAgADSw4AAlOx9wMjG43hcSBV4AI')
        keyboard_mark = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard= True)
        key_0 = types.KeyboardButton(text = '0')
        key_1 = types.KeyboardButton(text = '1')
        key_2 = types.KeyboardButton(text = '2')
        key_3 = types.KeyboardButton(text = '3')
        key_4 = types.KeyboardButton(text = '4')
        key_5 = types.KeyboardButton(text = '5')
        key_6 = types.KeyboardButton(text = '6')
        key_7 = types.KeyboardButton(text = '7')
        key_8 = types.KeyboardButton(text = '8')
        key_9 = types.KeyboardButton(text = '9')
        key_10 = types.KeyboardButton(text = '10')
        keyboard_mark.add(key_0, key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9, key_10)
        bot.send_message(message.from_user.id, "Привет, я бот-калькулятор, напиши первое число из своего примера", reply_markup= keyboard_mark)

        bot.register_next_step_handler(message, get_firstNum)
    elif message.text == '/help':
        bot.send_message(message.chat.id, "Привет!\nЯ бот, который умеет складывать числа.\nЧтобы запустить меня, пропиши команду /start.\nДля перехода на наш сайт пропиши команду /url")
    elif message.text == '/url':
        command_markup = types.InlineKeyboardMarkup()
        command_button = types.InlineKeyboardButton(text = 'Нажми на меня', url = 'https://www.instagram.com/mvstrike/')
        command_markup.add(command_button)
        bot.send_message(message.from_user.id, 'Если запутался, пропиши команду /help', reply_markup= command_markup)
    else:
        bot.send_sticker(message.from_user.id, 'CAADAgADfgcAAlSlcggAASP4YExETSQC')
        bot.send_message(message.from_user.id, "Написал не то, напиши /help")

def get_firstNum(message):
    global firstNum
    try:
        firstNum = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, "Я же просил ввести, число, будь добр, попробуй еще раз :)")
        bot.register_next_step_handler(message, get_firstNum)
        time.sleep(10)
    mark = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width=2)
    plus_button = types.KeyboardButton(text = "➕")
    minus_button = types.KeyboardButton(text = "➖")
    multiplication_button = types.KeyboardButton(text = "✖️")
    division_button = types.KeyboardButton(text = "➗")
    bot.send_sticker
    mark.add(plus_button, minus_button, multiplication_button, division_button)
    bot.send_message(message.from_user.id, 'Введите знак!', reply_markup= mark)


    bot.register_next_step_handler(message, get_point)

def get_point (message):
    global point
    point = message.text
    if (point != '+' and point != '-' and point != '*' and point == '/'):
        bot.send_message(message.from_user.id, 'Надо было ввести знак, для того, чтобы узнать правила ввода, можно нажать /help ')
        bot.register_next_step_handler(message, get_point)
    bot.send_message(message.from_user.id, 'Настало время ввести второе число!')
    bot.register_next_step_handler(message, get_secondNum)

def get_secondNum(message):
    global secondNum
    global result
    while secondNum == 0:

        try:
            secondNum = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Я же просил ввести, число, будь добр, попробуй еще раз :)")
            bot.register_next_step_handler(message, get_secondNum)
    if point == "➕":
        result = secondNum + firstNum
    elif point == "✖️":
        result = secondNum * firstNum
    elif point == "➖":
        result = firstNum - secondNum
    elif point == "➗":
        try:
            result = firstNum/ secondNum
        except Exception:
            bot.send_sticker(message.from_user.id, 'CAADAgADuwADCRdfAcMsM0OQwAFSAg')
    bot.send_sticker(message.from_user.id, 'CAADAgAD_gcAApkvSwq_CJ4u745t4gI')
    final = 'Твое первое число было: ' + str(firstNum) + '\nТвоё второе число было: ' + str(secondNum) + '\nТы решил выполнять действие: ' + str(point) +"\nИтого получилось: " + str(result)
    bot.send_message(message.from_user.id, final)
    url_markup = types.InlineKeyboardMarkup()
    url_button_1 = types.InlineKeyboardButton(text = 'Habr', url = 'https://habr.com/ru/')
    url_markup.add(url_button_1)
    url_button_2 = types.InlineKeyboardButton(text = 'PyTelegramBotAPI', url = 'https://github.com/eternnoir/pyTelegramBotAPI')
    url_markup.add(url_button_2)
    url_button_3 = types.InlineKeyboardButton(text = 'TelegramAPI', url = 'https://core.telegram.org/bots/api')
    url_markup.add(url_button_3)
    bot.send_message(message.from_user.id, "Бонусом ссылки на полезные ресурсы :)", reply_markup= url_markup)


def reset(message):
    global firstNum
    global secondNum
    global point
    global result
    if message.text == '/reset':
        firstNum = 0
        secondNum = 0
        point = ''
        result = 0
        bot.send_message(message.from_user.id, "Молодец, перезапустить бота, ты можешь с помощью ввода команды /reg")
    else:
        bot.send_message(message.from_user.id, "Ты што, не понял, если хочешь перезапустить, напиши /reset. Иначе у тебя будут вылетать лишние сообщения")




bot.polling(none_stop = True, interval = 0)



    #global jerk
    #jerk = message.text
    #bot.send_message(message.from_user.id, "Сос мыслом")
    #time.sleep(4)
    #keyboard = types.InlineKeyboardMarkup()
    #key_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'yes')
    #keyboard.add(key_yes)
    #key_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'no')
    #keyboard.add(key_no)
    #question = 'Когда дрочишь, ты бормочешь: '  + jerk + '. У тебя ' + str(money) + ' покемонов, и тебя зовут ' + name + '?'
    #bot.send_message(message.from_user.id, question, reply_markup = keyboard)

#@bot.callback_query_handler(func = lambda call:True)
#def callback_worker(call):
#    if call.data == 'yes':
#        bot.send_message(call.message.chat.id, 'Запомню :) ')
#    elif call.data == 'no':
#        bot.send_message(call.message.chat.id, 'Ну и пошел ты тогда, вводи нормально')
