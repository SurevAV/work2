from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext
from request.request_telegram import *

class InputPhone(StatesGroup):
    phone = State()

async def handler(
        message: types.Message, state: FSMContext):
    await message.answer(f"Введите номер вашего телефона.")
    await state.set_state(InputPhone.phone.state)


async def handler_2(
        message: types.Message, state: FSMContext):
    await state.finish()
    try:

        await send_to_user("5704787049", f'Пользователь с номером {message.text}, ид {message.chat.id}, юзернеймом {message.from_user.username} оплатил курс индивидульного обучения')
        await send_to_user("6145871916", f'Пользователь с номером {message.text}, ид  {message.chat.id}, юзернеймом {message.from_user.username} оплатил курс индивидульного обучения')
    except:
        pass
    await message.answer('''Если у Вас остались вопросы,
напишите мне @maxpolesu''')
