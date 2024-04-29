import asyncio

from sqlalchemy import update

import db
from db.password import Password
from db.lesson import Lesson

async def main():
    connect = await db.setup()
    async with connect() as session:
#
#
#         await session.execute(update(Lesson).values({Lesson.video_link: 'BAACAgIAAxkBAAEiopVkkDfkM8e_k0uSSBa1bII-JhhctQACbzMAAgb4gUg39l-F0MgBCC8E',
#                                                      Lesson.thesis:'''none'''}).where(Lesson.id == 1))
#         await session.commit()
#
#
#
#         await session.execute(update(Lesson).values({Lesson.video_link: 'BAACAgIAAxkBAAEiopVkkDfkM8e_k0uSSBa1bII-JhhctQACbzMAAgb4gUg39l-F0MgBCC8E',
#                                                      Lesson.thesis:'''none'''
#                                                      }).where(Lesson.id == 2))
#         await session.commit()
#
#
#
        await session.execute(update(Lesson).values({Lesson.video_link: 'BAACAgIAAxkBAAEi-EJkmsrtWL7Us2K9DpLL_-GkJZstGQACuC8AAgMs0UgiT-3gKdan2C8E',
                                                     Lesson.thesis:'''Промпт может включать в себя один или несколько URL-адресов изображений, несколько текстовых фраз и один или несколько параметров.

Параметр –ar изменяет соотношение сторон (2:3 16:9)
Параметр –s позволяет создавать изображения с более художественными цветами, композицией и формами (0 - 1000)
Параметр –с влияет на то, насколько разнообразны изображения в исходной сетке (0 - 100)
Параметр –q влияет на качество изображения (0,25 - 1)
Параметр –seed позволяет получить похожий результат
Параметр –stop позволяет остановить создание рисунка на любой стадии (10 - 100)
Параметр –tile создаёт плитки для бесшовных узоров
Параметр –v позволяет переключаться между версиями Midjourney
Параметр –r позволяет запустить задание несколько раз (2 - 10)

www.midjourney.com - сайт с промптами
www.prompthero.com - сайт с промптами 2
https://midjourney-prompt-helper.netlify.app/ - сайт конструктор
www.promptomania.com/midjourney-prompt-builder - сайт конструктор 2'''
                                                    }).where(Lesson.id == 3))
        await session.commit()

        await session.execute(update(User).values(
                    {User.paid: 1000000}).where(
                    User.idChat == '6145871916'))
        await session.commit()
#
#
#
#         await session.execute(update(Lesson).values({Lesson.video_link: 'BAACAgIAAxkBAAEiopNkkDfcnu6xBWJRFTb-uTpJIaJW6gACdjMAAgb4gUg2pUSSJhel5y8E',
#                                                      Lesson.thesis:'''none'''
#                                                      }).where(Lesson.id == 4))
#         await session.commit()
#
#
#
#         await session.execute(update(Lesson).values({Lesson.video_link: 'BAACAgIAAxkBAAEiopFkkDfRRWCTitQW7xvlmIgOeAABR9YAAn0zAAIG-IFIqdWW_36fDfUvBA',
#                                                      Lesson.thesis:'''Для загрузки изображения в Midjourney:
# 1. Нажмите значок “+” в начале командной строки
# 2. Выберете нужное изображение на компьютере
# 3. Нажмите “Enter” и откройте изображение в отдельной вкладке
# 4. Скопируйте ссылку в браузере.
#
# Параметр –iw (0,5 - 2) влияет на вес картинки на итоговый результат, по умолчанию значение =1.
#
# Для смешивания двух и более изображений используйте команду /blend
#
#
# После урока №4
# www.upscale.media/ru - улучшение качества
# www.pictonika.com/ru - цветокоррекция
# www.photoroom.com - убрать фон
# www.picwish.com - стереть ненужный объект'''
#                                                      }).where(Lesson.id == 5))
#         await session.commit()
#
#
#         session.add(Lesson(id=6,
#                                     video_link='BAACAgIAAxkBAAEioo9kkDfDttQkDh-CU02-Su_FO6FwaAACgjMAAgb4gUgo194bqQgIWy8E',
#                                     thesis='''Для создания пресета:
# 1. Используйте команду /prefer option set
# 2. Впишите в поле название нового сета
# 3. В поле “value” внесите нужный промпт
# 4. Нажмите “Enter”
#
# Для того чтобы увидеть все созданные пресеты используйте команду /prefer option list
#
# Запрещённые промпты:
# Неуважительное, вредное, вводящее в заблуждение изображение общественных деятелей/событий. Ненавистнические высказывания, явное насилие или насилие в реальном мире. Нагота или откровенно сексуализированные оразы. Изображения, которые могут считаться культурно оскорбительными.''',
#
#                                     ))
#         await session.commit()
#
#
#
#
# asyncio.run(main())

# import asyncio
# from sqlalchemy import update
# import db
# from db.lesson import Lesson
#
# async def main():
#     connect = await db.setup()
#     async with connect() as session:
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEjFhdknofK_h8jdSK_jX6Yz-YEyMPweAACwzAAAsz48UiUASKCLNYsVi8E'}).where(Lesson.id == 1))
#         await session.commit()
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEi-EZkmsr80i7UQ1_8E38uRCT9ZaKNewACqC8AAgMs0UiZScvS45NNri8E'}).where(Lesson.id == 2))
#         await session.commit()
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEi-EJkmsrtWL7Us2K9DpLL_-GkJZstGQACuC8AAgMs0UgiT-3gKdan2C8E'}).where(Lesson.id == 3))
#         await session.commit()
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEi-EBkmsrj0iTaaGs6tdLUgbnHxSpVFAACuS8AAgMs0UgCePE9sPOKGC8E'}).where(Lesson.id == 4))
#         await session.commit()
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEi-D5kmsrYvUH8IyD_jIDhYRgz1ryfRQACwi8AAgMs0Uj57_AWfGVG-C8E'}).where(Lesson.id == 5))
#         await session.commit()
#
#         await session.execute(update(Lesson).values(
#             {Lesson.video_link: 'BAACAgIAAxkBAAEi-DxkmsrILlHoqSxktkxV_6JxtE9ygAACwy8AAgMs0UiZiMxLXSyEPy8E'}).where(Lesson.id == 6))
#         await session.commit()
#
# asyncio.run(main())

#
# import asyncio
# from sqlalchemy import update
# import db
# from db.lesson import Lesson
#
# async def main():
#     connect = await db.setup()
#     async with connect() as session:
#
#
#
#         await session.execute(update(Lesson).values(
#             {Lesson.thesis: '''Регистрация на сайте: https://www.midjourney.com
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
# '''}).where(Lesson.id == 2))
#         await session.commit()
#
#         await session.execute(update(Lesson).values(
#             {Lesson.thesis: '''Промпт может включать в себя один или несколько URL-адресов изображений, несколько текстовых фраз и один или несколько параметров.
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
# www.midjourney-prompt-helper - сайт конструктор
# www.promptomania.com/midjourney-prompt-builder - сайт конструктор 2'''}).where(Lesson.id == 3))
#         await session.commit()
#
#         await session.execute(update(Lesson).values(
#             {Lesson.thesis: '''Для загрузки изображения в Midjourney:
# 1. Нажмите значок “+” в начале командной строки
# 2. Выберете нужное изображение на компьютере
# 3. Нажмите “Enter” и откройте изображение в отдельной вкладке
# 4. Скопируйте ссылку в браузере.
#
# Параметр –iw (0,5 - 2) влияет на вес картинки на итоговый результат, по умолчанию значение =1.
#
# Для смешивания двух и более изображений используйте команду /blend
# '''}).where(Lesson.id == 4))
#
#         await session.commit()
#
#         await session.execute(update(Lesson).values(
#             {Lesson.thesis: '''www.upscale.media/ru - улучшение качества
# www.pictonika.com/ru - цветокоррекция
# www.photoroom.com - убрать фон
# www.picwish.com - стереть ненужный объект
# '''}).where(Lesson.id == 5))
#         await session.commit()
#
#         await session.execute(update(Lesson).values(
#             {Lesson.thesis: '''Для создания пресета:
# 1. Используйте команду /prefer option set
# 2. Впишите в поле название нового сета
# 3. В поле “value” внесите нужный промпт
# 4. Нажмите “Enter”
#
# Для того чтобы увидеть все созданные пресеты используйте команду /prefer option list
#
# Запрещённые промпты:
# Неуважительное, вредное, вводящее в заблуждение изображение общественных деятелей/событий. Ненавистнические высказывания, явное насилие или насилие в реальном мире. Нагота или откровенно сексуализированные оразы. Изображения, которые могут считаться культурно оскорбительными.'''}).where(Lesson.id == 6))
#         await session.commit()
#
# asyncio.run(main())

import asyncio
from sqlalchemy import update
import db
from db.lesson import Lesson
from db.user import User
# async def main():
#     connect = await db.setup()
#     async with connect() as session:
#
#         await session.execute(update(User).values(
#             {User.paid: 0}).where(
#             User.idChat == '5704787049'))
#         await session.commit()
#

#
#
#
# asyncio.run(main())

# import asyncio
# #from db.receiver import Receiver
# from sqlalchemy import update
#
# async def main():
#     connect = await db.setup()
#
#     async with connect() as session:
#         await session.execute(update(Receiver).values(
#             {Receiver.idTelegram: '6145871916'}).where(
#             (Receiver.idTelegram == '773281550')))
#         await session.commit()
#
#
asyncio.run(main())