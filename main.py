import random
import time
import telebot
from telebot import types

bot = telebot.TeleBot('6056307341:AAF1izVzfCQ0szUIZpT0qdyaSlKp3pHNpV8')

level1_mes = """
Вы выбрали Уровень 1
Ваша задача решить 10 примеров
Максимальный ответ в примерах не превышает 25
Если вы решите правильно все 10 примеров, вы получите сертификат.
"""

level2_mes = """
Вы выбрали Уровень 2
Ваша задача решить 10 примеров
Максимальный ответ в примерах от 25 до 50
Если вы решите правильно все 10 примеров, вы получите сертификат.
"""

level3_mes = """
Вы выбрали Уровень 3
Ваша задача решить 10 примеров
Максимальный ответ в примерах от 50 до 100
Если вы решите правильно все 10 примеров, вы получите сертификат.
"""

level4_mes = """
Вы выбрали Уровень 4
Ваша задача решить 10 примеров
Максимальный ответ в примерах от 1 до 100
На ответ вам даётся 5 секунд
Если вы решите правильно все 10 примеров, вы получите сертификат.
"""


@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/level1")
    btn2 = types.KeyboardButton("/level2")
    btn3 = types.KeyboardButton("/level3")
    btn4 = types.KeyboardButton("/level4")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)


@bot.message_handler(commands=['level1'])
def level_1(message, num=1, score=0):
    if num == 1:
        bot.send_message(message.chat.id, level1_mes)
    if score == 10:
        img = open('Photo.PNG', 'rb')
        bot.send_photo(message.chat.id, img)
    if num > 10:
        bot.send_message(message.chat.id, "Вы решили все примеры! Количество правильных ответов: {}".format(score))
        return
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    otvet = num1 * num2
    sent = bot.send_message(message.chat.id, f"Пример {num}. Сколько будет {num1} x {num2}?")
    bot.register_next_step_handler(sent, review, otvet, num, num1, num2, score)


def review(message, otvet, num, num1, num2, score):
    message_to_save = message.text
    if message_to_save == str(otvet):
        bot.send_message(message.chat.id, "Верно")
        score += 1
        level_1(message, num + 1, score)
    else:
        bot.send_message(message.chat.id, "Неверно, правильный ответ {}".format(otvet))
        level_1(message, num + 1, score)


@bot.message_handler(commands=['level2'])
def level_2(message2, num_2=1, score_2=0):
    if num_2 == 1:
        bot.send_message(message2.chat.id, level2_mes)
    if score_2 == 10:
        img = open('Photo_2.png', 'rb')
        bot.send_photo(message2.chat.id, img)
    if num_2 > 10:
        bot.send_message(message2.chat.id, "Вы решили все примеры! Количество правильных ответов: {}".format(score_2))
        return
    num3 = random.randint(5, 7)
    num4 = random.randint(5, 7)
    otvet2 = num3 * num4
    sent2 = bot.send_message(message2.chat.id, f"Пример {num_2}. Сколько будет {num3} x {num4}?")
    bot.register_next_step_handler(sent2, review_2, otvet2, num_2, num3, num4, score_2)


def review_2(message2, otvet_2, num_2, num3, num4, score_2):
    message_to_save = message2.text
    if message_to_save == str(otvet_2):
        bot.send_message(message2.chat.id, "Верно")
        score_2 += 1
        level_2(message2, num_2 + 1, score_2)
    else:
        bot.send_message(message2.chat.id, "Неверно, правильный ответ {}".format(otvet_2))
        level_2(message2, num_2 + 1, score_2)


@bot.message_handler(commands=['level3'])
def level_3(message3, num_3=1, score_3=0):
    if num_3 == 1:
        bot.send_message(message3.chat.id, level3_mes)
    if score_3 == 10:
        img = open('Photo_3.png', 'rb')
        bot.send_photo(message3.chat.id, img)
    if num_3 > 10:
        bot.send_message(message3.chat.id, "Вы решили все примеры! Количество правильных ответов: {}".format(score_3))
        return
    num5 = random.randint(7, 10)
    num6 = random.randint(7, 10)
    otvet3 = num5 * num6
    sent3 = bot.send_message(message3.chat.id, f"Пример {num_3}. Сколько будет {num5} x {num6}?")
    bot.register_next_step_handler(sent3, review_3, otvet3, num_3, num5, num6, score_3)


def review_3(message3, otvet_3, num_3, num5, num6, score_3):
    message_to_save = message3.text
    if message_to_save == str(otvet_3):
        bot.send_message(message3.chat.id, "Верно")
        score_3 += 1
        level_3(message3, num_3 + 1, score_3)
    else:
        bot.send_message(message3.chat.id, "Неверно, правильный ответ {}".format(otvet_3))
        level_3(message3, num_3 + 1, score_3)


@bot.message_handler(commands=['level4'])
def level_4(message4, num_4=1, score_4=0):
    if num_4 == 1:
        bot.send_message(message4.chat.id, level4_mes)
    if score_4 == 10:
        img = open('Photo_4.png', 'rb')
        bot.send_photo(message4.chat.id, img)
    if num_4 > 10:
        bot.send_message(message4.chat.id, "Вы решили все примеры! Количество правильных ответов: {}".format(score_4))
        return
    num7 = random.randint(1, 10)
    num8 = random.randint(1, 10)
    otvet4 = num7 * num8
    sent4 = bot.send_message(message4.chat.id, f"Пример {num_4}. Сколько будет {num7} x {num8}?")
    bot.register_next_step_handler(sent4, review_4, otvet4, num_4, num7, num8, score_4)


def review_4(message4, otvet_4, num_4, num5, num6, score_4):
    message_to_save = message4.text
    start_time = time.time()
    if time.time() - start_time > 5:
        bot.send_message(message4.chat.id, "Вы не успели решить пример.")
        level_2(message4, num_4 + 1, score_4)
    if message_to_save == str(otvet_4):
        bot.send_message(message4.chat.id, "Верно")
        score_4 += 1
        level_4(message4, num_4 + 1, score_4)
    else:
        bot.send_message(message4.chat.id, "Неверно, правильный ответ {}".format(otvet_4))
        level_4(message4, num_4 + 1, score_4)


bot.polling()
