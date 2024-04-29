from sqlalchemy import select, update
from keyboards.keyboards import *
from aiogram.types import CallbackQuery
from aiogram import types
from db.user import User
from request.request_telegram import *

prices = [
    types.LabeledPrice(label='Оплата курсов', amount=275000),
]
#-------------------------------------------------------------------------------------------
async def pay(call: CallbackQuery):
    db = call.bot.get('db')
    async with db() as session:
        user = await session.execute(select(User).where(User.idTelegram == str(call.from_user.id)))
        user = user.fetchone()[0]

    if user.paid and user.paid >= 275000:
        await call.bot.send_message(call.from_user.id, "Оплата получена, переходите к изучению первого блока!",
                                       parse_mode='Markdown', reply_markup=make_keyboard([("Блок №1", 'lesson|1')]))
    else:
        await call.bot.send_invoice(call.from_user.id, title='Пополнение баланса',
                               description='Оплата курсов.',
                               provider_token=Config.PAYMENTS_PROVIDER_TOKEN,
                               currency='rub',
                               photo_url='https://telegra.ph/file/2c1f7fc68ad31a7415a7c.jpg',
                               photo_height=512,  # !=0/None or picture won't be shown
                               photo_width=512,
                               photo_size=512,
                               is_flexible=False,  # True If you need to set up Shipping Fee
                               prices=prices,
                               start_parameter='replenish-the-balance',
                               payload='ОПЛАТА')

async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await pre_checkout_query.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                        error_message="Aliens tried to steal your card's CVV,"
                                                      " but we successfully protected your credentials,"
                                                      " try to pay again in a few minutes, we need a small rest.")

async def got_payment(message: types.Message):
    payment_info = message.successful_payment.to_python()

    db = message.bot.get('db')

    async with db() as session:
        await session.execute(update(User).values({User.paid: payment_info['total_amount']}).where(
            User.idTelegram == str(message.from_user.id)))
        await session.commit()

    count = payment_info['total_amount']

    try:
        await send_to_user("5704787049", f'Пользователь {message.chat.id} {message.from_user.username} оплатил {str(count)}')
        await send_to_user("6145871916", f'Пользователь {message.chat.id} {message.from_user.username} оплатил {str(count)}')
    except:
        pass

    if payment_info['total_amount'] == 275000:

        await message.bot.send_message(message.chat.id, "Оплата получена, переходите к изучению первого блока!",
                                    parse_mode='Markdown', reply_markup=make_keyboard([("Блок №1", 'lesson|1')]))
    if payment_info['total_amount'] == 875000:
        await message.bot.send_message(message.chat.id, '''Оплата принята. Пожалуйста,
введите свой номер телефона
для того, чтобы обсудить
удобное время для обучения.''',
                                       parse_mode='Markdown',
                                       reply_markup=make_keyboard([("Ввести номер телефона", 'number')]))

