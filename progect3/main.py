import datetime
from flask import Flask, url_for, request, redirect, render_template, make_response, session, abort, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import json
import news_resources
import requests
from loginform import LoginForm
from data import db_session, news_api
from data.users import User
from data.news import News
from forms.user import RegisterForm
from forms.add_news import NewsForm
from mail_sender import send_mail
from dotenv import load_dotenv
import datetime

app = Flask(__name__)
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'too short key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/news.sqlite'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.errorhandler(404)
def http_404_error(error):
    return make_response(jsonify(({'error': f'Новости не найдена!'})), 404)


@app.errorhandler(400)
def http_400_error(error):
    return make_response(jsonify({'error': 'Некорректный запрос'}), 400)


@app.route('/error_404')
def well():
    return render_template('well.html')


@app.route('/')
@app.route('/index')
def index():
    # работу с БД начинаем с открытия сессии
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter((News.user == current_user) | (News.is_private != True))
        # print(News.user)
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template('index.html', title='Новости', news=news)

    # db_sess = db_session.create_session()
    # news = db_sess.query(News).filter(News.is_private != True)
    # return render_template('index.html', title='Новости', news=news)
    # param = {}
    # param['username'] = 'Студент'
    # param['title'] = 'Расширяем шаблоны'
    # return render_template('index.html', **param)
    # user = 'Студент'
    # return render_template('index.html', title='Работа с шаблоном', username=user)


@app.route('/news_del/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('news.html', title='Редактирование новости',
                           form=form)


@app.route('/ood_even')
def odd_even():
    return render_template('odd_even.html', number=8)


@app.route('/vartest')
def vartest():
    return render_template('var_test.html', title='Переменные в HTML')


@app.route('/news', methods=['GET', 'POST'])
@login_required
def news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()  # ORM-model News
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)  # слияние сессии с текущим пользователей
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости', form=form)

    # lst = ['ANN', 'TOM', 'BOB']
    # return render_template('news.html', news=lst)
    # with open('news.json', 'rt', encoding='utf-8') as f:
    #     news_list = json.loads(f.read())
    # return render_template('news.html', title='Новости', news=news_list)


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return f"""
        <form class="login_form" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="photo">Приложите фото:</label>
                <input type="file" class="from-control-file" id="photo" name="file">
            </div><br>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>          
        """
    elif request.method == 'POST':
        f = request.files['file']  # request.form.get('file')
        f.save('./static/images/loaded.png')
        return '<h1>Файл у Вас на сервере</h1>'


@app.route('/mail', methods=['GET'])
def get_form():
    return render_template('mail_send.html')


@app.route('/mail', methods=['POST'])
def post_form():
    email = request.values.get('email')
    if send_mail(email, 'Вам письмо', 'Текст письма'):
        return f'Письмо на адрес {email} отправлено успешно!'
    return 'Сбой при отправке'


@app.route('/poster')
def poster():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
<dl>
  <dt>Режиссер:</dt>
    <dd>Петр Точилин</dd>
<h1 class="red">Постер к фильму</h1>
<img src="{url_for('static', filename='images/kinogallery.com_Admiral_wall_1_1280.jpg')}"
alt="Здесь могла быть ваша картинка">
<p>Ибо крепка, как смерть, любовь!</p>
</body>
</html>"""


@app.route('/countdown')
def countdown():
    lst = [str(x) for x in range(10, 0, -1)]
    lst.append('Ибо крепка, как смерть, любовь!')
    return '<br>'.join(lst)


@app.route('/nekrasov')
def nekrasov():
    return f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
      <div class="alert alert-primary" role="alert">
        <p>Прости!</br> 
        Не помни дней паденья,</br>
        Тоски, унынья, озлобленья,-</br>
        Не помни бурь, не помни слез,</br>
        Не помни ревности угроз!</br></p>
    </div>
    <div class="alert alert-info" role="alert">
        Но дни, когда любви светило</br>
        Над нами ласково всходило</br>
        И бодро мы свершали путь,-</br>
        Благослови и не забудь!</br>
    </div>
"""


@app.route('/variants/<int:var>')
def variants(var):
    if var == 1:
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
<dl>
  <dt>Режиссер:</dt>
    <dd>Петр Точилин</dd>
<h1 class="red">Постер к фильму</h1>
<img src="{url_for('static', filename='images/kinogallery.com_Admiral_wall_1_1280.jpg')}"
alt="Здесь могла быть ваша картинка">
<p>Ибо крепка, как смерть, любовь!</p>
</body>
</html>"""
    elif var == 2:
        return f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Постер</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
        <dt>В ролях:</dt>
            <dd>Андрей Гайдулян</dd>
            <dd>Алексей Гаврилов</dd>
            <dd>Виталий Гогунский</dd>
            <dd>Мария Кожевникова</dd>
        </dl>
        <h1 class="red">Постер к фильму</h1>
        <img src="{url_for('static', filename='images/kinogallery.com_Admiral_wall_1_1280.jpg')}"
        alt="Здесь могла быть ваша картинка">
        <p>Ибо крепка, как смерть, любовь!</p>
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
        </body>
        </html>"""


@app.route('/slogan')
def slogan():
    return 'Ибо крепка, как смерть, любовь! <br><a href="/">Назад</a>'


@app.route('/slideshow')
def slideshow():
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Постер</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="{url_for('static', filename='1-leg.jpg')}">
            </div>
            <div class="carousel-item">
              <img src="{url_for('static', filename='2-leg.jpg')}">
            </div>
            <div class="carousel-item">
              <img src="{url_for('static', filename='3-leg.jpg')}">
            </div>
          </div>
          <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Предыдущий</span>
          </a>
          <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Следующий</span>
          </a>
        </div>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
    </body>
    </html>"""


@app.route('/form_sample', methods=['GET', 'POST'])
def form_sample():
    if request.method == 'GET':
        return render_template('userform.html', title='Форма')
        # with open('./templates/userform.html', 'r', encoding='utf-8') as html_stream:
        #     return html_stream.read()
    elif request.method == 'POST':
        # добавить картинку
        myform = request.form.to_dict()
        return render_template('filled_form.html', title='Ваши данные', data=myform)


@app.route('/weather_form', methods=['GET', 'POST'])
def weather_form():
    if request.method == 'GET':
        return render_template('weather_form.html', title='Выбор города')
    elif request.method == 'POST':
        town = request.form.get('town')
        data = {}
        key = '1e7fb1ea6ff110200166ea0703c535ca'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()
        code = weather['cod']
        icon = weather['weather'][0]['icon']
        temperature = weather['main']['temp']
        data['temp'] = int(temperature)
        data['icon'] = icon
        data['code'] = code
        return render_template('weather.html', title=f'Погода в городе {town}', town=town, data=data)


@app.route('/success')
def success():
    return 'Success'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html', title='Повторите, пожалуйста', message='Неверный логин или пароль',
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Проблема', message='Восстановите пароль', form=form)
        db_sess = db_session.create_session()  # цепляемся к БД
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Проблема с регистрации', message='Такой пользователь уже '
                                                                                            'существует', form=form)
        user = User(name=form.name.data, email=form.email.data, about=form.about.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count != 0 and visit_count <= 20:
        res = make_response(f'Были уже {visit_count + 1} раз')
        res.set_cookie('visit_count', str(visit_count + 1), max_age=60 * 60 * 24 * 365)
    # else:
    #     res = make_response('Вы впервые здесь за год')
    #     res.set_cookie('visit_count', '1', max_age=60 * 60 * 24 * 365)
    elif visit_count > 20:
        res = make_response(f'Были уже {visit_count + 1} раз')
        res.set_cookie('visit_count', '1', max_age=0)
    else:
        res = make_response('Вы впервые здесь за год')
        res.set_cookie('visit_count', '1', max_age=60 * 60 * 24 * 365)
    return res


@app.route('/session_test')
def session_test():
    visit_count = session.get('visit_count', 0)
    session['visit_count'] = visit_count + 1
    if session['visit_count'] > 3:
        session.pop('visit_count')
    session.permanent = True
    return make_response(f'Мы тут были уже {visit_count + 1} раз')


if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    # подключаем api с помощью blueprint
    # app.register_blueprint(news_api.blueprint)
    #подключаем api с помощью flask-restful
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:mews_ida>')

    app.run(host='127.0.0.1', port=5000, debug=True)

    # # user = User()
    # # user.name = 'Vlad'
    # # user.about = '23 years old'
    # # user.email = 'vlad@mail.ru'
    # db_sess = db_session.create_session()
    # id = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title='Новость 3', content='Описание новости', user_id=id.id, is_private=False)
    # # db_sess.add(news)
    # id.news.append(news)
    # db_sess.commit()
    # # users = db_sess.query(User).filter(User.name.ilike('%d%'))
    # # users = db_sess.query(User).all()
    # # db_sess.commit()
    # # user = db_sess.query(User).filter(User.id == 2).first()
    # # user = db_sess.query(User).filter(User.name == 'Anna').first()
    # # user.name = "Pavel"
    # # db_sess.delete(user)
    # # db_sess.commit()
