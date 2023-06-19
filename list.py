from flask import Flask, render_template, request, make_response
import datetime
import uuid


app = Flask(__name__)

@app.route("/",methods=['Get', "POST"]  )
def main_page( ):

    ip = 'None'
    if request.environ.get('HTTP_X_FORWARDED_FOR'):
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.environ['REMOTE_ADDR']

    cookie = 'None'
    if not request.cookies.get('user'):
        cookie = f'{str(uuid.uuid4())} ; {ip} ; {str(datetime.datetime.now())[:19]}'
    else:
        cookie = str(request.cookies.get('user'))

    item = ' '
    if request.method == 'POST':

        panel_input = request.form['panel_input']
        panel_text = request.form['panel_text']
        file_object = open('items.txt', 'a')
        file_object.write(f'{str(datetime.datetime.now())[:19]} ip- {ip} cookie- {cookie} from- {panel_input} item- {panel_text}\n')
        file_object.close()
        item = '-'


    file_object = open('users.csv', 'a')
    file_object.write(f'{ip} ; {cookie} ; {str(datetime.datetime.now())[:19]}; {item};\n')
    file_object.close()


    if not request.cookies.get('user'):
        res = make_response(render_template("MainPage.html"))
        res.set_cookie('user', cookie, expires=datetime.datetime.now() + datetime.timedelta(days=365))
        return res


    return render_template("MainPage.html")
