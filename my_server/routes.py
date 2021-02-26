from typing import NoReturn
from my_server import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, session
from my_server.forms import LoginFrom, RegistrationFrom
from my_server.dbhandler import User, Mail
from flask_login import LoginManager
from RandomWordGenerator import RandomWord

app.config['SECRET_KEY'] = 'b9dfdf3f8d2bb591f39d5a1337dbacd0'


def gotmail():
    if 'mail' in session.keys():
        return True
    return False


def newMail():
    rw = RandomWord(constant_word_size=10)
    newmail = rw.generate()
    newmail += '@gluffa.se'
    return newmail


@app.route('/')
@app.route('/start', methods=['GET'])
def start():
    if gotmail():
        return render_template('start.html', mail=session['mail'], title='Start')
    else:
        return render_template('start.html', mail=newMail(), title='Start')

    


@app.route('/login', methods=['POST', 'GET'])
def login():

    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            #login_user(user, remember=form.rememberme.data)
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
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign up!', form=form)


@app.route('/logout')
def logout():
    return render_template('mails')

@app.route('/email', methods=['POST'])
def recieve_mail():
    print("tjo katt")

    new_mail = Mail(sender=request.form['from'], to=request.form['to'], subject=request.form['subject'], body=request.form['text'])
    db.session.add(new_mail)
    db.session.commit()
    print('From:', request.form['from'])
    print('To:', request.form['to'])
    print('Subject:', request.form['subject'])
    print('Body:', request.form['text'])
    return ''