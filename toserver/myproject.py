import asyncio

from sqlalchemy import update

import db
from db.password import Password
from db.lesson import Lesson

async def main():
    connect = await db.setup()
    async with connect() as session:
        await session.execute(update(Lesson).values({Lesson.video_link: 'none2'}).where(Lesson.id == 1))
        await session.commit()


        await session.execute(update(Lesson).values({Lesson.video_link: 'BAACAgIAAxkBAAEimdFkjv1JKoHwe7OIlPE1J0kOfRHIiQACfCsAAndOeEirB7YAAYdOFbgvBA'}).where(Lesson.id == 2))
        await session.commit()


        await session.execute(update(Lesson).values({Lesson.video_link: 'BAACAgIAAxkBAAEimdNkjv1S_kQ_HrPatEucZbuXKAW8kgACdCsAAndOeEgcfNOTZvVN_S8E'}).where(Lesson.id == 3))
        await session.commit()

        await session.execute(update(Lesson).values({Lesson.video_link: 'BAACAgIAAxkBAAEimdVkjv1bT-iJR-eGjU5rp_xkcVmQrQACaisAAndOeEglEyKYpoulxS8E'}).where(Lesson.id == 4))
        await session.commit()


        await session.execute(update(Lesson).values({Lesson.video_link: 'BAACAgIAAxkBAAEimddkjv1n9mDJVZDND3X5ym0eqZcYuAACZCsAAndOeEgKZTOKC2hfGy8E'}).where(Lesson.id == 5))
        await session.commit()

    # async with connect() as session:
    #
    #     session.add(Password(text='it1234'))
    #     await session.commit()


#     async with connect() as session:
#
#         session.add(Lesson(id=1,
#                            video_link = 'none',
#                            thesis='none',
#                            answers = '0',
#                            right_answer = 0,
#                            ))
#         await session.commit()
#
#         session.add(Lesson(id=2,
#                            video_link='https://drive.google.com/file/d/1xOowYxd953yoUlxEBaVt24GEWAQm0JSj/view?usp=drive_link',
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
# www.midjourney-prompt-helper - сайт конструктор
# www.promptomania.com/midjourney-prompt-builder - сайт конструктор 2''',
#                            answers='0',
#                            right_answer=0,
#                            ))
#         await session.commit()
#
#         session.add(Lesson(id=3,
#                            video_link='https://drive.google.com/file/d/1eiZIkYDN8VxsYaofGkNJg23R0oTIQpjv/view?usp=drive_link',
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
#                            answers='0',
#                            right_answer=0,
#                            ))
#         await session.commit()
#
#         session.add(Lesson(id=4,
#                            video_link='https://drive.google.com/file/d/15GmOmtVg7CEAyO3WWPvoG2ZLtU4SimXo/view?usp=drive_link',
#                            thesis='''www.upscale.media/ru - улучшение качества
# www.pictonika.com/ru - цветокоррекция
# www.photoroom.com - убрать фон
# www.picwish.com - стереть ненужный объект''',
#                            answers='0',
#                            right_answer=0,
#                            ))
#         await session.commit()
#
#         session.add(Lesson(id=5,
#                            video_link='https://drive.google.com/file/d/19Ki6fdMfRADM9B4N19wDozQiO-gzyTGB/view?usp=drive_link',
#                            thesis='none',
#                            answers='0',
#                            right_answer=0,
#                            ))
#         await session.commit()





asyncio.run(main())