from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Привет, я приложение Flask'

#http://localhost:5000/countdown

@app.route('/countdown')
def countdown():
    cl = ['Start']
    cl += [str(x) for x in reversed(range(11))]
    cl.append('finish')
    return '<br>'.join(cl)

@app.route('/contacts')
def contacts():
    return """
    <b>E-mail:</b>a@b.ru<br>
    <b>Address:</b>St.Petersburg<br>
    <a href='/'>На главную</a>
    """

#статический контент (в папке static/..)
# все изображения
#таблицы стилей, шрифты - static/fonts, любые файлы для скачивания,
# фалый JS-сценариев, музыка, видео
#для удобства польуземся url_for

@app.route('/img/<num>')
def show_img(num):
    """
    :param num:по умоплчанию - строка
    <int:num> - целое число
    <float:num> - Действительное число
    <path:num> - строка со слешами для URL
    <uuid:num> - идектификатор в 16м представлении()
    :return: путь к картинке

    """
    return f"""
    <h1>Python</h1>
    <img src="{url_for('static', filename=f'images/python-{num}.jpg')}">
    """

@app.route('/two-params/<username>/<int:number>')
def two_params_func(username, number):
    param = 100 + number
    return f"""
    <h1>Пользователь {username}</h1>
    <h2>номер в системе {param}</h2>
    """



if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')