from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Regexp
from db.lesson import Lesson
from sqlalchemy import func
from sqlalchemy import select, update
from keyboards.keyboards import *
from aiogram.types import CallbackQuery
from db.user import User
from datetime import datetime
from aiogram.types.message import ContentTypes
from . import pay
from . import pay2
from . import input_phone
def setup(db: Dispatcher):

    db.register_message_handler(bot_start, CommandStart())
    db.register_callback_query_handler(step_2, text='step_2')
    db.register_callback_query_handler(step_3, text='step_3')
    db.register_callback_query_handler(step_4, Regexp(regexp='step_4.*'))

    db.register_callback_query_handler(step_5, text='step_5')
    db.register_callback_query_handler(step_6, text='step_6')
    db.register_callback_query_handler(step_7, text='step_7')
    db.register_callback_query_handler(step_8, text='step_8')
    db.register_callback_query_handler(step_9, text='step_9')
    db.register_callback_query_handler(step_10, text='step_10')
    db.register_callback_query_handler(end, text='end')

    db.register_callback_query_handler(lesson, Regexp(regexp='lesson.*'))
    # #---------------------------------------------------------------------------------------
    db.register_callback_query_handler(pay.pay,text='pay')
    db.register_pre_checkout_query_handler(pay.checkout, lambda query: True)
    db.register_message_handler(pay.got_payment,content_types=ContentTypes.SUCCESSFUL_PAYMENT)
    # ---------------------------------------------------------------------------------------

    # #---------------------------------------------------------------------------------------
    db.register_callback_query_handler(pay2.pay2, text='pay2')
    db.register_pre_checkout_query_handler(pay2.checkout2, lambda query: True)
    # ---------------------------------------------------------------------------------------

    db.register_callback_query_handler(thesis, Regexp(regexp='thesis.*'))

    db.register_callback_query_handler(input_phone.handler, text='number')
    db.register_message_handler(
        input_phone.handler_2,
        state=input_phone.InputPhone.phone)



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
    await call.message.answer('''Вас ждёт самый актуальный и
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

    #await call.bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.bot.send_video(call.from_user.id, video=lesson.video_link,
                              reply_markup=make_keyboard([("Далее", 'step_4')]),
                              supports_streaming=True)


async def step_4(call: CallbackQuery):

    list_buttons = [("Хочу доступ к видеоурокам", 'pay'),
                    ("Хочу индивидуальное обучение с экспертом", 'step_5'),
                    ("У меня остались вопросы", 'step_6'),]

    text = '''Присоединяйся к каналу
https://t.me/neirofun

Для вашего удобства
предусмотрено два формата
обучения: очное занятие с
экспертом в онлайн формате с
помощью Zoom или Skipe, а
также самостоятельное
изучение подготовленных для
вас видеоуроков.'''

    if len(call.data.split('|'))<2:
        await call.message.answer(text, reply_markup=make_keyboard(list_buttons), disable_web_page_preview=True)
    else:
        await call.message.answer(text, reply_markup=make_keyboard(list_buttons), disable_web_page_preview=True)


async def step_5(call: CallbackQuery):

    list_buttons = [("Перейти к оплате", 'pay2'),
                    ("Назад", 'step_4|again')
                    ]

    await call.message.answer('''Индивидуальное обучение
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


    await call.message.answer('''Для вашего удобства
предусмотрено два формата
обучения: очное занятие с
экспертом в онлайн формате с
помощью Zoom или Skipe, а
также самостоятельное
изучение подготовленных для
вас видеоуроков.''', reply_markup=make_keyboard(list_buttons))


async def step_7(call: CallbackQuery):
    await call.message.answer('''Нет, курс записан на русском, а
для работы достаточно иметь
под рукой онлайн-переводчик.''', reply_markup=make_keyboard([("Понятно", 'step_4|again')]))

async def step_8(call: CallbackQuery):
    await call.message.answer('''Никакого дополнительного
софта не потребуется, обучение
проходит в этом боте, а для
работы достаточно любого
браузера.''', reply_markup=make_keyboard([("Понятно", 'step_4|again')]))

async def step_9(call: CallbackQuery):
    await call.message.answer('''Даже если изучать по одному
уроку в день, уже через неделю
Вы будете обладать новым
уникальным навыком!''', reply_markup=make_keyboard([("Понятно", 'step_4|again')]))


async def step_10(call: CallbackQuery):
    await call.message.answer('''Стоимость индивидуального
обучения с экспертом
составляет *8750р*. 

Доступ к обучающим 
видеоурокам - всего *2750р.*''', parse_mode= 'Markdown',reply_markup=make_keyboard([("Перейти к оплате видеоуроков", 'pay'),
                                               ("Перейти к оплате индивидуального обучения ", 'pay2'),
                                               ("Назад", 'step_4|again')]))

async def end(call: CallbackQuery):
    await call.message.answer('''Поздравляю Вас с
прохождением курса "MJ.
Основы нейроиллюстрации"!
Теперь Вы можете
самостоятельно создавать
шедевры с помощью Midjourney.
Если остались вопросы,
напишите мне @maxpolesu и я
обязательно постараюсь
помочь.''')

async def lesson_query(call, number):
    db = call.bot.get('db')
    async with db() as session:
        lesson = await session.execute(select(Lesson).where(Lesson.id == number))
        lesson = lesson.fetchone()[0]
    return lesson


async def lesson(call: CallbackQuery):
    number_lesson = int(call.data.split('|')[1])+1
    lesson = await lesson_query(call,number_lesson)

    db = call.bot.get('db')
    async with db() as session:
        await session.execute(update(User).values({User.lesson: number_lesson}).where(User.idTelegram == str(call.from_user.id)))
        await session.commit()

    await call.bot.send_video(call.from_user.id, video=lesson.video_link,
                              reply_markup=make_keyboard([(f"Ключевые тезисы {str(number_lesson-1)} блока", f'thesis|{str(number_lesson)}')]),
                              supports_streaming=True)
async def thesis(call: CallbackQuery):
    number_lesson = int(call.data.split('|')[1])
    lesson = await lesson_query(call,number_lesson)

    db = call.bot.get('db')
    async with db() as session:
        count = await session.execute(select(func.count(Lesson.id)))
        count = count.fetchone()[0]


    if number_lesson < count:
        await call.message.answer(lesson.thesis, reply_markup=make_keyboard([(f"Блок №{str(number_lesson)}", f'lesson|{str(number_lesson)}')]), disable_web_page_preview=True)
    else:
        await call.message.answer(lesson.thesis, reply_markup=make_keyboard([("Завершить", 'end')]), disable_web_page_preview=True)

