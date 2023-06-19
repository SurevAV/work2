from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Regexp
from db.lesson import Lesson
from db.user import User
from keyboards.keyboards import *
from aiogram.types import CallbackQuery
from sqlalchemy.future import select
from sqlalchemy import update, func
from data.config import Config
import requests
from datetime import datetime
def setup(db: Dispatcher):

    db.register_message_handler(bot_start, CommandStart())
    db.register_callback_query_handler(step_2, text='step_2')
    db.register_callback_query_handler(step_3, text='step_3')
    #db.register_callback_query_handler(step_4, text='step_4')
    db.register_callback_query_handler(step_4, Regexp(regexp='step_4.*'))

    db.register_callback_query_handler(step_5, text='step_5')
    db.register_callback_query_handler(step_6, text='step_6')
    db.register_callback_query_handler(step_7, text='step_7')
    db.register_callback_query_handler(step_8, text='step_8')
    db.register_callback_query_handler(step_9, text='step_9')
    db.register_callback_query_handler(step_10, text='step_10')
    # db.register_callback_query_handler(bot_start_again, text='lesson_down|main')

async def bot_start(call: CallbackQuery):
    db = call.bot.get('db')

    async with db() as session:
        user = await session.execute(select(User).where(User.idTelegram == str(call.from_user.id)))
        if not user.fetchone():
            session.add(User(name=call.from_user.username,
                             lesson=0,
                             idTelegram=str(call.from_user.id),
                             lastDate=datetime.now(),
                             idChat=str(call.from_user.id)))
        else:
            await session.execute(
                update(User).values({User.name: call.from_user.username,
                                     User.lastDate: datetime.now(),
                                     User.idChat: str(call.from_user.id)
                                     }).where(User.idTelegram == str(call.from_user.id)))
        await session.commit()

    await call.answer('''Привет! Этот обучающий бот
поможет тебе в кратчайшие
сроки изучить нейросеть
Midjourney и начать
профессионально использовать
её возможности.''', reply_markup=make_keyboard([("Начать", 'step_2')]))


async def step_2(call: CallbackQuery):
    await call.message.edit_text('''Вас ждёт самый актуальный и
полный практический
видеокурс по Midjourney,
состоящий из пяти видеоуроков
и краткого текстового описания
к ним.''', reply_markup=make_keyboard([("Смотреть превью", 'step_3')]))



async def step_3(call: CallbackQuery):
    db = call.bot.get('db')
    async with db() as session:
        lesson = await session.execute(select(Lesson).where(Lesson.id == 1))
        lesson = lesson.fetchone()[0]

    await call.bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.bot.send_video(call.from_user.id, video=lesson.video_link,
                              reply_markup=make_keyboard([("Далее", 'step_4')]),
                              supports_streaming=True)


async def step_4(call: CallbackQuery):

    list_buttons = [("Хочу доступ к видеоурокам", 'pay'),
                    ("Хочу индивидуальное обучение с экспертом", 'step_5'),
                    ("У меня остались вопросы", 'step_6'),]

    text = '''Для вашего удобства
предусмотрено два формата
обучения: очное занятие с
экспертом в онлайн формате с
помощью Zoom или Skipe, а
также самостоятельное
изучение подготовленных для
вас видеоуроков.'''

    if len(call.data.split('|'))<2:
        await call.message.answer(text, reply_markup=make_keyboard(list_buttons))
    else:
        await call.message.edit_text(text, reply_markup=make_keyboard(list_buttons))


async def step_5(call: CallbackQuery):

    list_buttons = [("Перейти к оплате", 'pay'),
                    ("Назад", 'step_4|again')
                    ]

    await call.message.edit_text('''Индивидуальное обучение
состоит из трёх онлайн занятий
с экспертом, длительностью до
1 часа. Вы освоите все базовые и
продвинутые способы создания
иллюстраций в Midjourney, а
также получите все пять уроков
из видеокурса.''', reply_markup=make_keyboard(list_buttons))



async def step_6(call: CallbackQuery):

    list_buttons = [("Нужно ли знание английского?", 'step_7'),
                    ("Какие программы мне потребуются?", 'step_8'),
                    ("Сколько времени займёт обучение?", 'step_9'),
                    ("Какая стоимость?", 'step_10'),
                    ("Вернуться", 'step_4|again')]


    await call.message.edit_text('''Для вашего удобства
предусмотрено два формата
обучения: очное занятие с
экспертом в онлайн формате с
помощью Zoom или Skipe, а
также самостоятельное
изучение подготовленных для
вас видеоуроков.''', reply_markup=make_keyboard(list_buttons))


async def step_7(call: CallbackQuery):
    await call.message.edit_text('''Нет, курс записан на русском, а
для работы достаточно иметь
под рукой онлайн-переводчик.''', reply_markup=make_keyboard([("Понятно", 'step_4|again')]))

async def step_8(call: CallbackQuery):
    await call.message.edit_text('''Никакого дополнительного
софта не потребуется, обучение
проходит в этом боте, а для
работы достаточно любого
браузера.''', reply_markup=make_keyboard([("Понятно", 'step_4|again')]))

async def step_9(call: CallbackQuery):
    await call.message.edit_text('''Даже если изучать по одному
уроку в день, уже через неделю
Вы будете обладать новым
уникальным навыком!''', reply_markup=make_keyboard([("Понятно", 'step_4|again')]))


async def step_10(call: CallbackQuery):
    await call.message.edit_text('''Стоимость индивидуального
обучения с экспертом
составляет 8750р. Доступ к
видеоурокам стоит не дороже
чем подписка Midjourney на
месяц - 2750р.''', reply_markup=make_keyboard([("Перейти к оплате", 'pay'), ("Назад", 'step_4|again')]))







#     db.register_callback_query_handler(lesson_up, Regexp(regexp='lesson_up.*'))
#     db.register_callback_query_handler(lesson_down, Regexp(regexp='lesson_down.*'))
#     db.register_callback_query_handler(thesis, Regexp(regexp='thesis.*'))
#
#
#
# #query---------------------------------------------
# async def update_user_lesson(call, lesson):
#     db = call.bot.get('db')
#     async with db() as session:
#         await session.execute(
#             update(User).values({User.lesson: int(lesson),
#                                  User.name: call.from_user.username,
#                                  User.lastDate: datetime.now(),
#                                  User.idChat: str(call.from_user.id)}
#                                 ).where(User.idTelegram == str(call.from_user.id)))
#         await session.commit()
#
# async def lesson_query(call, lesson):
#     db = call.bot.get('db')
#     async with db() as session:
#         lesson_row = await session.execute(select(Lesson).where(Lesson.id == lesson))
#         lesson_row = lesson_row.fetchone()[0]
#     return lesson_row
#
# async def start(call):
#     db = call.bot.get('db')
#
#     async with db() as session:
#         user = await session.execute(select(User).where(User.idTelegram == str(call.from_user.id)))
#         if not user.fetchone():
#             session.add(User(name=call.from_user.username,
#                              lesson=0,
#                              idTelegram=str(call.from_user.id),
#                              lastDate=datetime.now(),
#                              idChat=str(call.from_user.id)))
#         else:
#             await session.execute(
#                 update(User).values({User.name: call.from_user.username,
#                                      User.lastDate: datetime.now(),
#                                      User.idChat: str(call.from_user.id)
#                                      }).where(User.idTelegram == str(call.from_user.id)))
#         await session.commit()
#
#     list_buttons = (("Начать урок", 'lesson_up|0'),
#                     ("Приобрести курс", '-'))
#     return list_buttons
# #query---------------------------------------------
#
#
# async def thesis(call: CallbackQuery):
#     lesson = int(call.data.split('|')[1])
#     lesson_row = await lesson_query(call, lesson)
#     #await call.bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
#
#     await call.message.answer(f'Урок {lesson}:  {lesson_row.thesis}',
#                                  reply_markup=make_keyboard([], f'lesson_up|{str(lesson-1)}'))
#
#
#
# async def lesson_up(call: CallbackQuery):
#     db = call.bot.get('db')
#     lesson = int(call.data.split('|')[1])+1
#
#     async with db() as session:
#         count = await session.execute(select(func.count(Lesson.id)))
#         count = count.fetchone()[0]
#
#
#
#     list_buttons = [("Тезис", f'thesis|{str(lesson)}')]
#     if lesson>=count:
#         lesson = int(count)
#     else:
#         list_buttons.append(("Следующий урок", f'lesson_up|{str(lesson)}'))
#
#
#     back = lesson
#     if lesson == 1:
#         back = 'main'
#
#     await update_user_lesson(call, lesson)
#     lesson_row = await lesson_query(call, lesson)
#
#     try:
#         #await call.bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
#         await call.bot.send_video(call.from_user.id, video=lesson_row.video_link, caption= f'Урок: {str(lesson)}' ,reply_markup=make_keyboard(list_buttons, f'lesson_down|{str(back)}'), supports_streaming=True)
#     except:
#         #await call.bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
#         await call.message.answer(f'Урок {lesson}  {lesson_row.video_link}', reply_markup=make_keyboard(list_buttons, f'lesson_down|{str(back)}'))
#
# async def lesson_down(call: CallbackQuery):
#     lesson = int(call.data.split('|')[1]) - 1
#
#
#     back = lesson
#     if lesson == 1:
#         back = 'main'
#
#     await update_user_lesson(call, lesson)
#     lesson_row = await lesson_query(call, lesson)
#     list_buttons = (("Тезис", f'thesis|{str(lesson)}'),
#                     ("Следующий урок", f'lesson_up|{str(lesson)}'))
#
#     try:
#         await call.bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
#         await call.bot.send_video(call.from_user.id, video=lesson_row.video_link, caption= f'Урок: {str(lesson)}',
#                                   reply_markup=make_keyboard(list_buttons, f'lesson_down|{str(back)}'),
#                                   supports_streaming=True)
#     except:
#         await call.bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
#         await call.message.answer(f'Урок {lesson}  {lesson_row.video_link}',
#                                   reply_markup=make_keyboard(list_buttons, f'lesson_down|{str(back)}'))
#
#
# async def bot_start(call: CallbackQuery):
#     list_buttons = await start(call)
#     await call.answer(f"Приветсвую хотите начать урок?", reply_markup=make_keyboard(list_buttons,''))
#
# async def bot_start_again(call: CallbackQuery):
#     list_buttons = await start(call)
#     await call.message.edit_text(f"Приветсвую хотите начать урок?", reply_markup=make_keyboard(list_buttons,''))
