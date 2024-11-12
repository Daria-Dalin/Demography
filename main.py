from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['content'] = 'Этот текст отобразится на главной странице'
    param['title'] = 'Главная'
    return render_template('index.html', **param)


   # """
   # <a href="/index">Главная</a> | <a href="/contacts">Контакты</a>
    # | <a href="/img/1">Картинка 1</a>
    # | <a href="/img/2">Картинка 2</a>
   # """

@app.route('/news')

def news():
    with open("news.json", "rt", encoding="utf-8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list, title='news')

@app.route('/odd_even/', defaults={'num': 0})
@app.route('/odd_even/<int:num>')
def odd_even(num):
    return render_template('index.html', num=num, title='четное или нечетное')


# http://localhost:5000/countdown

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


# статический контент (в папке static/..)
# все изображения
# таблицы стилей, шрифты - static/fonts, любые файлы для скачивания,
# фалый JS-сценариев, музыка, видео
# для удобства польуземся url_for

@app.route('/img/', defaults={'num': None})
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
    if num:
        return f"""
        <h1>Python</h1>
        <img src="{url_for('static',
                           filename=f'images/python-{num}.jpg')}"><br>
        <a href="/index">Главная</a>
        """
    else:
        return f"""
        <h1>здесь ничего нет</h1>
        <img src="{url_for('static',
                           filename='images/python.png')}"><br>
        <a href="/index">Главная</a>
        """


@app.route('/two-params/<username>/<int:number>')
def two_params_func(username, number):
    param = 100 + number
    return f"""
    <h1>Пользователь {username}</h1>
    <h2>номер в системе {param}</h2>
    """
#Методы
# GET - запрашивает информацию с сервера не меняя его состояния
# POST - отправляет даннные на сервер для обработки
# PUT - заменяет текущие данные на сервере данными запроса
# PATCH - частичная замена данных на сервере
# DELETE - удаляет указанные данные

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
            <title>Заполните форму</title>
            <link rel="stylesheet" href="css/style.css">
            <link type="image/png" sizes="32x32" rel="icon" href="./images/favicon.png">
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.6.0/css/all.css">
        </head>
        <body>
        <!--Главный контейнер-->
        <div class="container">
            <h1>форма для регистрации</h1>
            <form class="form-control" method="post">
                <input class="form-control" type="email" name="email" id="email" placeholder="введите email">
                <input class="form-control" type="password" name="password" id="password">
                <label for="profSelect">Ваша профессия</label>
                <select class="form-control" name="profession" id="profSelect">
                    <option>Инженер</option>
                    <option>Конструктор</option>
                </select>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
        </div>
        <!--Главный контейнер end-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz"
                crossorigin="anonymous"></script>
        </body>
        </html>     
        """
    #elif request.method == 'POST':
      #  print(request.form['email'])
      #  print(request.form['password'])
       # print(request.form['profession'])
      #  return 'Форма успешно отправлена'
    elif request.method == 'POST':
        return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
                  integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
            <title>Заполните форму</title>
            <link rel="stylesheet" href="css/style.css">
            <link type="image/png" sizes="32x32" rel="icon" href="./images/favicon.png">
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.6.0/css/all.css">
        </head>
        <body>
        <!--Главный контейнер-->
        <div class="container">
            <h1>Вот что вы отправили</h1>
           <p><b>Ваш email: </b>{request.form['email']}</p>
            <p><b>Ваш пароль: </b>{request.form['password']}</p>
            <p><b>Ваша профессия: </b>{request.form['profession']}</p>
        </div>
        <!--Главный контейнер end-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz"
                crossorigin="anonymous"></script>
        </body>
        </html>
        """

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
