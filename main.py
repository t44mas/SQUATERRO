from flask import Flask, render_template
from flask_login import LoginManager

from data import db_session
from data.users import User
from form.register import RegisterForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(int(user_id))

@app.route('/')
def list_of_work():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return render_template('main.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # if form.validate_on_submit():
    #     if form.password.data != form.password_again.data:
    #         return render_template('register.html', title='Регистрация',
    #                                form=form,
    #                                message="Пароли не совпадают")
    #     db_sess = db_session.create_session()
    #     if db_sess.query(User).filter(User.email == form.email.data).first():
    #         return render_template('register.html', title='Регистрация',
    #                                form=form,
    #                                message="Такой пользователь уже есть")
    #     user = User(
    #         email=form.email.data,
    #         surname=form.surname.data,
    #         name=form.name.data,
    #         age=form.age.data,
    #         position=form.position.data,
    #         speciality=form.speciality.data,
    #         address=form.address.data,
    #     )
    #     user.set_password(form.password.data)
    #     db_sess.add(user)
    #     db_sess.commit()
    #     return redirect('/')
    return render_template('register.html', form=form)

def main():
    db_session.global_init("db/cooking.db")
    # app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()