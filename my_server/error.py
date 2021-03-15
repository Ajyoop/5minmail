from my_server import app
from flask import render_template

@app.errorhandler(401)
def not_authenticated(error):
    return render_template('error.html', error_code='401', error_message='Not Authenticated'), 401

@app.errorhandler(404)
def file_not_found(error):
    return render_template('error.html', error_code='404', error_message='File not Found'), 404


