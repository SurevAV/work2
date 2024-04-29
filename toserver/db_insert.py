# import asyncio
#
# from sqlalchemy import update
#
# import db
# from db.password import Password
# from db.lesson import Lesson
#
#
# async def main():
#     connect = await db.setup()
#     async with connect() as session:
#         session.add(Password(text='it1234'))
#         await session.commit()
#         print(1)
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEjlKtkrpI-tpL01sYEtrPsr2d91fQWlAACnS8AAnlLeUkt4fgYmpBJqy8E',Lesson.thesis:'''none'''}).where(Lesson.id == 1))
#
#         #----------------------------------------
#
#         session.add(Lesson(video_link='BAACAgIAAxkBAAEjFhdknofK_h8jdSK_jX6Yz-YEyMPweAACwzAAAsz48UiUASKCLNYsVi8E',
#                            thesis = 'none',
#                            id=1))
#         await session.commit()
#         print(2)
#
#         session.add(Lesson(video_link='BAACAgIAAxkBAAEi-EZkmsr80i7UQ1_8E38uRCT9ZaKNewACqC8AAgMs0UiZScvS45NNri8E',
#                            thesis='''Регистрация на сайте: https://www.midjourney.com
# /imagine  - создать изображение
# /info - информация об аккаунте и подписке
# /settings - настройки
# /describe - получить текстовое описание картинки
#
# Кнопки U под сеткой изображений отвечают за улучшение картинки.
# Кнопки V под сеткой изображений позволяют получить вариации картинки
#
# Способы оплаты. Если у Вас нет зарубежной карты, то можно воспользоваться следующими сервисами:
# https://pay-saas.ru/
# https://oplatazabugor.ru/
# https://remoney.ru/1382-midjourney.html
# https://telegra.ph/Karta-inostrannogo-banka-04-20
# Или напишите Дмитрию @diver91 указав промокод “FORFUN”.''',
#                            id=2))
#         await session.commit()
#         print(3)
#
#         session.add(Lesson(video_link='BAACAgIAAxkBAAEi-EJkmsrtWL7Us2K9DpLL_-GkJZstGQACuC8AAgMs0UgiT-3gKdan2C8E',
#                            thesis='''Промпт может включать в себя один или несколько URL-адресов изображений, несколько текстовых фраз и один или несколько параметров.
#
# Параметр –ar изменяет соотношение сторон (2:3 16:9)
# Параметр –s позволяет создавать изображения с более художественными цветами, композицией и формами (0 - 1000)
# Параметр –с влияет на то, насколько разнообразны изображения в исходной сетке (0 - 100)
# Параметр –q влияет на качество изображения (0,25 - 1)
# Параметр –seed позволяет получить похожий результат
# Параметр –stop позволяет остановить создание рисунка на любой стадии (10 - 100)
# Параметр –tile создаёт плитки для бесшовных узоров
# Параметр –v позволяет переключаться между версиями Midjourney
# Параметр –r позволяет запустить задание несколько раз (2 - 10)
#
# www.midjourney.com - сайт с промптами
# www.prompthero.com - сайт с промптами 2
# https://midjourney-prompt-helper.netlify.app/ - сайт конструктор
# www.promptomania.com/midjourney-prompt-builder - сайт конструктор 2''',
#                            id=3))
#         await session.commit()
#         print(4)
#
#         session.add(Lesson(video_link='BAACAgIAAxkBAAEi-EBkmsrj0iTaaGs6tdLUgbnHxSpVFAACuS8AAgMs0UgCePE9sPOKGC8E',
#                            thesis='''Для загрузки изображения в Midjourney:
# 1. Нажмите значок “+” в начале командной строки
# 2. Выберете нужное изображение на компьютере
# 3. Нажмите “Enter” и откройте изображение в отдельной вкладке
# 4. Скопируйте ссылку в браузере.
#
# Параметр –iw (0,5 - 2) влияет на вес картинки на итоговый результат, по умолчанию значение =1.
#
# Для смешивания двух и более изображений используйте команду /blend
# ''',
#                            id=4))
#         await session.commit()
#         print(5)
#
#         session.add(Lesson(video_link='BAACAgIAAxkBAAEi-D5kmsrYvUH8IyD_jIDhYRgz1ryfRQACwi8AAgMs0Uj57_AWfGVG-C8E',
#                            thesis='''www.upscale.media/ru - улучшение качества
# www.pictonika.com/ru - цветокоррекция
# www.photoroom.com - убрать фон
# www.picwish.com - стереть ненужный объект''',
#                            id=5))
#         await session.commit()
#         print(6)
#
#         session.add(Lesson(video_link='BAACAgIAAxkBAAEi-DxkmsrILlHoqSxktkxV_6JxtE9ygAACwy8AAgMs0UiZiMxLXSyEPy8E',
#                            thesis='''Для создания пресета:
# 1. Используйте команду /prefer option set
# 2. Впишите в поле название нового сета
# 3. В поле “value” внесите нужный промпт
# 4. Нажмите “Enter”
#
# Для того чтобы увидеть все созданные пресеты используйте команду /prefer option list
#
# Запрещённые промпты:
# Неуважительное, вредное, вводящее в заблуждение изображение общественных деятелей/событий. Ненавистнические высказывания, явное насилие или насилие в реальном мире. Нагота или откровенно сексуализированные оразы. Изображения, которые могут считаться культурно оскорбительными.''',
#                            id=6))
#         await session.commit()
#         print(7)
#
#
#
#
# asyncio.run(main())

import asyncio

from sqlalchemy import update

import db
from db.password import Password
from db.lesson import Lesson


# async def main():
#     connect = await db.setup()
#     async with connect() as session:
#
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEjlKtkrpI-tpL01sYEtrPsr2d91fQWlAACnS8AAnlLeUkt4fgYmpBJqy8E'}).where(
#             Lesson.id == 1))
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEjlK9krpJ7QJvk2KUxv7rtzn2odM5xQwACoC8AAnlLeUk929U_AZCAjS8E'}).where(
#             Lesson.id == 2))
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEjlL9krpRQb3qWa9Nv9vSUpZWTJjHy5wACrS8AAnlLeUkLstzfusg6UC8E'}).where(
#             Lesson.id == 3))
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEjlMNkrpR8WpP_wlrdTR7SnlLBlGnitwACri8AAnlLeUmbPCCMnvV4iS8E'}).where(
#             Lesson.id == 4))
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEjlMhkrpTLTA1L48HnnLr_y3mofQFCqgACtC8AAnlLeUka9d6SMHIVNy8E'}).where(
#             Lesson.id == 5))
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEjlM5krpUgp6zsIlnFrIvyeKaKM-btNQACuS8AAnlLeUnWxp7e-U0o6i8E'}).where(
#             Lesson.id == 6))
#
#
#
#         #----------------------------------------
#         await session.commit()
#
#
#
#
#
#
#
# asyncio.run(main())


import asyncio
from sqlalchemy import update
import db
from db.user import User
async def main():
    connect = await db.setup()
    async with connect() as session:

        await session.execute(update(User).values(
            {User.paid: 1000000}).where(
            User.idChat == '5704787049'))
        await session.commit()





asyncio.run(main())