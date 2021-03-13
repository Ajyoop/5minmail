from my_server import app, db, bcrypt, socketio
from flask import render_template, url_for, flash, redirect, request, session
from my_server.forms import LoginFrom, RegistrationFrom
from my_server.dbhandler import User, Mail
from flask_login import login_user, current_user, logout_user, login_required
from RandomWordGenerator import RandomWord
from flask_socketio import SocketIO, emit, send
import json

app.config['SECRET_KEY'] = 'b9dfdf3f8d2bb591f39d5a1337dbacd0'


def gotmail():
    if 'mail' in session.keys():
        return True
    return False


def newMail():
    rw = RandomWord(max_word_size=10)
    newmail = rw.generate()
    newmail += '@gluffa.se'
    session['mail'] = newmail
    return newmail


@app.route('/')
@app.route('/index')
@app.route('/start', methods=['GET'])
def start():
    if not gotmail():
        return render_template('start.html', mailadd=newMail(), title='Start')
    return render_template('start.html', mailadd=session['mail'], title='Start')
    


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('start'))
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.rememberme.data)
            flash('You have been logged in', 'success')
            print('23213333333333')
            return redirect(url_for('start'))
        else:
            print('asddddddddddddddddddd')
            flash('Incorrect email or password', 'danger')
    return render_template('login.html', title='5minmail', form=form)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Account created. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign up!', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have benn logged out', 'success')
    return redirect(url_for('start'))

@app.route('/email', methods=['POST'])
def recieve_mail():
    new_mail = Mail(sender=request.form['from'], to=request.form['to'], subject=request.form['subject'], body=request.form['text'])
    db.session.add(new_mail)
    db.session.commit()
    return ''


def getMails(receiver):
    return Mail.query.filter_by(to=receiver)


def serializeAll(mails):
    maildict = []
    for mail in mails:
        maildict.append(mail.serialize)
    return maildict

@socketio.on('message')
def refeshdata(data):
    print('received message: ' + data)

@socketio.on('mailrefresh')
def mailrefresh():
    data = json.dumps(serializeAll(getMails(session['mail'])))
    print(data)
    socketio.emit('mailrefresh', data)