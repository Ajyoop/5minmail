from my_server import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from my_server.forms import LoginFrom, RegistrationFrom
from my_server.dbhandler import User
from random_word import RandomWords



app.config['SECRET_KEY'] = 'b9dfdf3f8d2bb591f39d5a1337dbacd0'


@app.route('/')
@app.route('/start', methods=['GET'])
def start():
    r = RandomWords()
    newmail = r.get_random_word()
    newmail += '@gluffa.se'
    return render_template('start.html', newmail=newmail)


@app.route('/login')
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
           # login_user(user, remember=form.rememberme.data)
            flash('You have been logged in', 'success')
            return redirect(url_for('start'))
        else:
            flash('yeety retard')
    return render_template('login.html', title='5minmail', form=form)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Account created. Please log in.', 'success')
        return redirect(url_for('start'))
    return render_template('signup.html', form=form)


@app.route('/mails')
def recieve_mail():
    return render_template('mails')


