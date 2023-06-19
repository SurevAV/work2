from flask import request
from flask import render_template, make_response, send_file
import uuid
from db.user import User
from db.login import Login
from db.password import Password
from sqlalchemy.future import select
from data.config import Config
import requests
from datetime import datetime, timedelta
from flask import Flask, redirect, url_for
import db
from sqlalchemy import update, func


app = Flask(__name__)


db_worker = db
async def send_to_user(chat, text):
    token = Config.BOT_TOKEN
    chat_id = chat
    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    return requests.get(url_req)




@app.route("/login", methods=["Get", "POST"])
async def login():
    db = await db_worker.setup()

    if request.method == 'POST':
        

        async with db() as session:
            check = await session.execute(select(Password).where(Password.text == request.form['panel_input']))
            check = check.fetchone()

        if check:
            token = str(uuid.uuid4())
            async with db() as session:
                session.add(Login(token=token, toDate = datetime.now()+timedelta(minutes=30)))
                telegram_response = await session.commit()
               

            res = make_response(redirect(url_for('main_page')))
            res.set_cookie('user', token)
            return res
        else:
            res = make_response(render_template("page1.html", password='Не правильный пароль. Введите пароль'))
            res.set_cookie('user', 'item')
            return res


    res = make_response(render_template("page1.html", password = 'введите пароль'))
    res.set_cookie('user', 'item')
    return res


async def main_page_response():
    count_users = 0
    db = await db_worker.setup()

    status_telegram_response = "Введите текст сообщения"
    # --------------------------------
    if request.method == 'POST':
        if request.form['panel_input']:
            
            status_telegram_response = await send_to_user(request.form['panel_input'], request.form['text_input'])

            if str(status_telegram_response) == '<Response [400]>':
                status_telegram_response = "Не удалось отправить сообщение"
            else:
                status_telegram_response = "Введите текст сообщения"
        else:
            async with db() as session:
                users = await session.execute(select(User))
                users = users.fetchall()

            for user in users:
                await send_to_user(user[0].idChat, request.form['text_input'])
    # --------------------------------

    elif request.method == "GET" and request.args.get("from") and request.args.get("to"):

        date_from = datetime.strptime(request.args.get("from"), '%Y-%m-%d')
        date_to = datetime.strptime(request.args.get("to"), '%Y-%m-%d')

       

        if request.args.get("csv"):
            async with db() as session:
                users = await session.execute(
                    select(User).where((User.lastDate >= date_from) & (User.lastDate <= date_to)))
                users = users.fetchall()
            if users:

                csv = open("visitors.csv", "w")
                for item in users:
                    row = [item[0].name,item[0].lastDate]
                    csv.write(";".join([str(x) for x in row]) + "\n")
                csv.close()
                return send_file("visitors.csv", as_attachment=True)
        elif request.args.get("select"):
            async with db() as session:
                count = await session.execute(select(func.count(User.id)).where((User.lastDate >= date_from) & (User.lastDate <= date_to)))
                count_users = count.fetchone()[0]

    else:
        date_from = datetime.strptime('2023-05-04', '%Y-%m-%d')
        date_to = datetime.strptime('2025-10-01', '%Y-%m-%d')

        async with db() as session:
            count = await session.execute(
                select(func.count(User.id)).where((User.lastDate >= date_from) & (User.lastDate <= date_to)))
            count_users = count.fetchone()[0]



    return render_template("page2.html", count_users=str(count_users), status_telegram_response=status_telegram_response)


@app.route("/", methods=["Get", "POST"])
async def main_page():
    db = await db_worker.setup()

    if request.cookies.get('user'):
        async with db() as session:
            check = await session.execute(select(Login).where(
                (Login.token == request.cookies.get('user')) & (Login.toDate>datetime.now())
            ))
            check = check.fetchone()
        if check:
            return await main_page_response()

        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


if __name__ == "__main__":

    app.run(threaded=True, host='0.0.0.0', port=5020)