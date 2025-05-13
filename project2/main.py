# from tkinter import Tk, Button
# from PIL import ImageTk, Image
#
#
# class MyButton(Button):
#     def __init__(self, pict, command):
#         self.image = Image.open(pict)
#         self.image = self.image.resize((100, 100))
#         self.pict = ImageTk.PhotoImage(self.image)
#         super().__init__(image=self.pict, command=command)
#
#
# root = Tk()
# root.geometry('800x600')
# root.title('Красная кнопка')
# image = 'slon.jpg'
# pict = ImageTk.PhotoImage(file=image)
# # Button(root, image=pict, command=lambda: print('click')).pack()
#
# MyButton(image, command=lambda: print('click')).pack()
# root.mainloop()
# import asyncio
# import os
# import time
# from datetime import datetime
#
#
# def dish(num, prepare, wait):
#     print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%H:%M:%S")}. Приготовление {prepare} мин.')
#     time.sleep(prepare)
#     print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%H:%M:%S")}. Ожидание {num} {wait} мин.')
#     time.sleep(wait)
#     print(f'В  {datetime.now().strftime("%H:%M:%S")} блюдо {num} готово.')
#
#
# async def main():
#     tasks = [
#         async.create_task(dish(1, 2, 3)),
#         async.create_task(dish(2, 5, 10)),
#         async.create_task(dish(3, 3, 5)),
#     ]
#     await asyncio.gather(*tasks)
#
#
# t0 = time.time()
# dish(1, 2, 3)
# dish(2, 5, 10)
# dish(3, 3, 5)
# delta = int(time.time() - t0)
# print(f' в {datetime.now().strftime("%H:%M:%S")} мы закончили')
# print(f'Затраченное время {delta}')

# Бот-телега
import logging
# import telebot
import config
# from telebot import types
import logging  # фиксация действий
import config
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

# Запустим логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_buttons = [
    ['/address', '/site'],
    ['/help', '/start']
]

TIMER = 5

markup = ReplyKeyboardMarkup(reply_buttons, one_time_keyboard=False)


def remove_job(name, context):
    current_job = context.job_queue.get_jobs_by_name(name)
    if not current_job:
        return False
    for job in current_job:
        job.schedule_removal()
    return True


"""
Функция обработки сообщений
update - принимает
context - доп. информация о сообщении 
"""


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def start(update, context):
    """
    Реакция на команду /start
    """
    user = update.effective_user
    await update.message.reply_html(
        rf'Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-то.',
        reply_markup=markup
    )


async def set_timer(update, context):
    chat_id = update.effective_message.chat_id
    job_removed = remove_job(str(chat_id), context)
    context.job_queue.run_once(task, TIMER,
                               chat_id=chat_id,
                               name=str(chat_id),
                               data=TIMER)
    text = f'Буду через {TIMER} сек!'
    if job_removed:
        text += ' Старая задача удалена.'
    await update.effective_message.reply_text(text)


async def task(context):
    await context.bot.send_message(context.job.chat_id,
                                   text=f'Вот и прошли {TIMER} сек.')


async def help_command(update, context):
    await update.message.reply_text('Я простой справочник')


async def unset(update, context):
    chat_id = update.message.chat_id
    job_removed = remove_job(str(chat_id), context)
    text = 'Таймер отменён' if job_removed else 'Таймеры не были установлены'
    await update.message.reply_text(text)


async def address(update, context):
    await update.message.reply_text('Адрес ИПАП: СПб, Можайская, 2')


async def site(update, context):
    await update.message.reply_text('https://google.com')


async def close_keyboard(update, context):
    await update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())


def main():
    application = Application.builder().token(config.bot_token).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('address', address))
    application.add_handler(CommandHandler('site', site))
    application.add_handler(CommandHandler('close', close_keyboard))
    application.add_handler(CommandHandler('set', set_timer))
    application.add_handler(CommandHandler('unset', unset))
    application.run_polling()


if __name__ == '__main__':
    main()

# name = ''
# surname = ''
# age = 0
#
# bot = telebot.TeleBot(config.bot_token)
#
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/start':
#         bot.send_message(message.from_user.id, 'Как тебя зовут?')
#         bot.register_next_step_handler(message, get_name)
#     else:
#         bot.send_message(message.from_user.id, 'Я вас не поняла, напишите /start')
#
#
# def get_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, 'Сколько Вам лет?')
#     bot.register_next_step_handler(message, get_age)
#
#
# def get_age(message):
#     global age
#     while age == 0:
#         try:
#             age = int(message.text)
#         except ValueError:
#             bot.send_message(message.from_user.id, 'Введите ваш возраст?')
#             age = 1
#             break
#     question = f'Тебе {age} лет, и ты {name} {surname}?'
#     keyboard = types.InlineKeyboardMarkup()
#     yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
#     keyboard.add(yes)
#     no = types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(no)
#     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#     # bot.send_message(message.from_user.id, 'Введите ваш возраст?')
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     global age
#
#     if call.data == "yes":
#         bot.send_message(call.message.chat.id, 'Приятно познакомиться')
#     elif call.data == "no":
#         age = 0
#         bot.send_message(call.message.chat.id, 'Начать сначала')
#         bot.register_next_step_handler(call.message, get_name)
#
#
# def get_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message(message.from_user.id, 'Ваше фамилия?')
#     bot.register_next_step_handler(message, get_surname)
#
#
# @bot.message_handler(commands=['start'])  # реагирует на /start
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     but1 = types.InlineKeyboardButton('Приветствую!')
#     but2 = types.InlineKeyboardButton('Задать вопрос!')
#     markup.add(but1, but2)
#     bot.send_message(message.chat.id, 'Привет, {0.first_name}! Нажать'.format(message.from_user), reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if message.text == 'Приветствую!':
#         bot.send_message(message.chat.id, text='Привет. Спасибо, что посетили нас!')
#     elif message.text == 'Задать вопрос!':
#         markup = types.InlineKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.InlineKeyboardButton('Как меня зовут?')
#         btn2 = types.InlineKeyboardButton('Чем могу помочь?')
#         back = types.InlineKeyboardButton('Назад в главное меню')
#         markup.add(btn1, btn2, back)
#         bot.send_message(message.chat.id, text='Задать вопрос!', reply_markup=markup)
#     elif message.text == 'Как меня зовут?':
#         bot.send_message(message.chat.id, text='Я всего лишь бот!')
#     elif message.text == 'Чем могу помочь?':
#         bot.send_message(message.chat.id, text='Привет!')
#     elif message.text == 'Назад в главное меню':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.InlineKeyboardButton('Поздороваться')
#         button2 = types.InlineKeyboardButton('Задать вопрос')
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text='Вы вернулись в главное меню', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, text='Я не знаю такой команды')
#
#
# bot.polling(none_stop=True)
