import datetime

from flask import (Flask, url_for, request, render_template,
                   redirect, flash, make_response, session, abort, jsonify)
from werkzeug.utils import secure_filename

from forms.add_news import NewsForm
from forms.loginform import LoginForm
from mailform import MailForm
import json, os
import configparser
from data import db_session
from data.users import User
from data.news import News
from forms.user import RegisterForm
from flask_login import (LoginManager, login_user,
                         logout_user, login_required, current_user)
from data.news import News
import news_api

import requests

MS1 = 'http://127.0.0.1:5000/api/news'

current_directory = os.path.dirname(__file__)  # путь к корню сервера
UPLOAD_FOLDER = f'{current_directory}/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'too_short_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

config = configparser.ConfigParser()


# ORM - Object Relational Mappin - Объектно-реляционное отображение

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.errorhandler(401)
def http_401_handler(error):
    return render_template('error401.html', title='Требуется аутентификация')


@app.errorhandler(404)
def http_404_handler(error):
    return make_response(jsonify({'error': 'Новость не найдена'}), 404)
   # return render_template('error404.html', title='Контент не найден')

@app.errorhandler(400)
def http_400_handler(_):
    return make_response(jsonify({'error': 'Новость не найдена'}), 400)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['text'] = 'Этот текст отобразится на главной странице'
    param['title'] = 'Главная'
    return render_template('index.html', **param)


@login_manager.user_loader
def user_loader(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


# """
# <a href="/index">Главная</a> | <a href="/contacts">Контакты</a>
# | <a href="/img/1">Картинка 1</a>
# | <a href="/img/2">Картинка 2</a>
# """

@app.route('/session_test')
def session_test():
    visit_count = session.get('visit_count', 0)
    session['visit_count'] = visit_count + 1
    return make_response(f'Вы посетили данную страницу {visit_count} раз')


@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count:
        res = make_response(
            f'Вы посетили данную страницу {visit_count + 1} раз')
        res.set_cookie('visit_count', str(visit_count + 1), max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response('За последние 2 года вы посетили данную страницу впервые')
        res.set_cookie('visit_count', '1', max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf-8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list, title='news')


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'GET':
        return render_template('weather.html', title='Погода в городе {city}', form=None)
    elif request.method == 'POST':
        config.read('settings.ini')
        city = request.form['city']
        if len(city) < 2:
            flash('Город не введен или введен не полностью')
            return redirect(request.url)
        key = config['Weather']['key']

        res = requests.get('http://api.openweathermap.org/data/2.5/find',
                           params={'q': city,
                                   'type': 'like',
                                   'units': 'metric',
                                   'APPID': key})
        data = res.json()
        if len(data['list']) == 0:
            flash('Город неверно')
            return redirect(request.url)
        temp = data['list'][0]['main']
        params = {'temper': temp['temp'],
                  'feel': temp['feels_like'],
                  'press': temp['pressure'],
                  'humid': temp['humidity']}  # пустой словарь для передачи параметров в render weather.html

        return render_template('weather.html',
                               title=f'Погода в {city}',
                               form=request.form, params=params)


@app.route('/apitest')
def api_test():
    res = requests.get('MS1').json()
    return render_template('apitest.html', title='Тестируем наш первый API', news=res['news'])


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   title='Регистрация',
                                   form=form, message='Пароли не совпадают')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message=f'Пользователь с Email {form.email.data} уже есть')
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')  # request.urlлибо на нужную страницу
        return render_template('login.html', title='Ошибка авторизации',
                               message='Неправильная пара: логин-пароль!',
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/blog')
    return render_template('add_news.html',
                           title='Добавление новости', form=form)


@app.route('/blog/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()

        if news:
            form.title.data = news.title
            form.content = news.content
            form.is_private.data = news.is_private
            form.submit.data = 'Отредактировать'
        else:
            abort(404)

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()

        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/blog')
        else:
            abort(404)
    return render_template('add_news.html', title='Редактирование новости',
                           form=form)


@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()

    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/blog')


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = MailForm()
    params = {}
    if form.validate_on_submit():
        name = form.username.data
        params['name'] = name
        phone = form.phone.data
        params['phone'] = phone
        email = form.email.data
        params['email'] = email
        message = form.message.data
        params['message'] = message
        params['page'] = request.url

        text = f"""
        Пользователь {name} оставил вам сообщение:
        {message}
        Его телефон {phone}
        {email}
        Страница: {request.url}
        """
        text_to_user = f"""
       Уважаемый (-ая) {name}!
       Ваши данные:
       Телефон: {phone}
       E-mail: {email}
       успешно получены.
       Ваше сообщение:
       {message}
       принято к рассмотрению.
       Отправлено со страницы: {request.url}
        """
        # send_mail(email, 'Ваши данные на сайте', text_to_user)
        # send_mail('мой email', 'Запрос с сайта', text)
        return render_template('/meilresult.html',
                               title='Ваши данные', params=params)
    return render_template('contacts.html',
                           title='Наши контакты', form=form)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('upload.html', title='Выбор файла', form=None)
    elif request.method == 'POST':
        if 'file' not in request.files:
            flash('Файл не был прочитан')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Файл не был отправлен')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('Загрузка файлов данного типа запрещена!')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('upload.html', title='Файл загружен',
                                   form=True)


@app.route('/success')
@login_required
def success():
    return 'Успех'


@app.route('/pets')
def pets():
    with open("pets.json", "rt", encoding="utf-8") as f:
        pets_list = json.load(f)
    print(pets_list)
    return render_template('pets.html', pets=pets_list, title='pets')


@app.route('/queue')
def queue():
    return render_template('queue.html', title='Очередь на медосмотр')


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


# 1. требуемый пункт меню
# 2. создать .html-файл для расширения шаблона
# 3. Отрендерить, осздав соответсвующий декоратор
@app.route('/about')
def about():
    params = {}
    params['title'] = 'Обо мне'
    params['text'] = ''
    return render_template('about.html', **params)


@app.route('/blog')
def blog():
    # if current_user.is_admin():
    # else
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private == False)
    return render_template('blog.html', title='Новости',
                           news=news)


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


# Методы
# GET - запрашивает информацию с сервера не меняя его состояния
# POST - отправляет даннные на сервер для обработки
# PUT - заменяет текущие данные на сервере данными запроса
# PATCH - частичная замена данных на сервере
# DELETE - удаляет указанные данные

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('form_sample.html', title='Заполните форму', form='None')

    elif request.method == 'POST':
        return render_template('form_sample.html', title='Ваши данные', form=request.form)


if __name__ == '__main__':
    db_session.global_init('db/blogs.db')
    # прописываем blueprint
    app.register_blueprint(news_api.blueprint)
    app.run(port=5000, host='127.0.0.1')

    # news create
    # db_sess = db_session.create_session()
# news = News(title="Первая новость", content="Первая новость",
#      user_id=1, is_private=False)
# db_sess.add(news)
#  db_sess.commit()

# read news
# news = db_sess.query(News).filter(News.user_id == 1).first()
# print(news.title)

# CRUD#create user
# user = User()
# user.name = 'User3'
# user.about = 'Третий пользователь нашей БД'
# user.email = 'email3@email.ru'
# db_sess = db_session.create_session()
# db_sess.add(user)
# db_sess.commit()
# read
# for user in db_sess.query(User).all():
#    print(user)
# print(user.name)
# result = db_sess.query(User).filter(User.id > 1, User.email.notlike("%1%"))
# for user in result:
#   print(print.name, user.email)
# update
# result = db_sess.query(User).filter(User.id == 2).first()
# result.name = 'User22'

# result.create_date = datetime.datetime.now()
# db_sess.commit()
# print(result.name)


# delete
# db_sess.query(User).filter(User.id == 2).delete()
# db_sess.commit()

# user = db_sess.query(User).filter(User.id >1).delete()
# db_sess.commit()
