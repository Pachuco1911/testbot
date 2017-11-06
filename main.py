import telebot
import constants
import random
import get_schedule
import time
bot = telebot.TeleBot(constants.token)

print(bot.get_me())

def log(message, answer):
    print("\n", constants.line)
    from datetime import datetime
    print(datetime.now())
    print(constants.log_message.format(message.from_user.first_name,
                                        message.from_user.last_name,
                                        str(message.from_user.id),
                                        message.text))
    print("Ответ:", answer)



@bot.message_handler(commands=['start'])
def handle_text(message):
    sticker = constants.sticker_start
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id, constants.start_message.format(message.from_user.first_name,
                                                                     message.from_user.last_name))
    answer = constants.start_message.format(message.from_user.first_name,
                                            message.from_user.last_name)
    log(message, answer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    sticker = random.choice(constants.sticker_fuckoff)
    bot.send_sticker(message.chat.id, sticker)
    time.sleep(2)
    bot.send_message(message.chat.id, constants.help_message)
    answer = constants.help_message
    log(message, answer)


@bot.message_handler(commands=['stop'])
def handle_text(message):
    sticker = random.choice(constants.sticker_like)
    bot.send_sticker(message.chat.id, sticker)
    answer = "like_sticker"
    log(message, answer)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if get_schedule.schedule(message.text)!='':
        bot.send_message(message.chat.id, get_schedule.schedule(message.text))
        answer = get_schedule.schedule(message.text)
        log(message, answer)
    else:
        sticker = random.choice(constants.sticker_wat)
        bot.send_sticker(message.chat.id, sticker)
        bot.send_message(message.chat.id, constants.error_wrong_gr_num)
        answer = get_schedule.schedule(message.text)
        log(message, answer)

bot.polling(none_stop=True, interval=0)