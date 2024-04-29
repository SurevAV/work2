from sqlalchemy import select
from keyboards.keyboards import *
from aiogram.types import CallbackQuery
from aiogram import types
from data import Config
from db.user import User

prices = [
    types.LabeledPrice(label='Оплата курсов', amount=875000),
]
#-------------------------------------------------------------------------------------------
async def pay2(call: CallbackQuery):
    db = call.bot.get('db')
    async with db() as session:
        user = await session.execute(select(User).where(User.idTelegram == str(call.from_user.id)))
        user = user.fetchone()[0]

    if user.paid and user.paid >= 875000:
        await call.bot.send_message(call.from_user.id, '''Оплата принята. Пожалуйста,
введите свой номер телефона
для того, чтобы обсудить
удобное время для обучения.''',
                                       parse_mode='Markdown', reply_markup=make_keyboard([("Ввести номер телефона", 'number')]))
    else:
        await call.bot.send_invoice(call.from_user.id, title='Пополнение баланса',
                               description='Оплата курсов индивидуального обучения.',
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

async def checkout2(pre_checkout_query: types.PreCheckoutQuery):
    await pre_checkout_query.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                        error_message="Aliens tried to steal your card's CVV,"
                                                      " but we successfully protected your credentials,"
                                                      " try to pay again in a few minutes, we need a small rest.")

