from my_server import app

class Config:
    app.config['SECRET_KEY'] = '82809d5e386a0a0f5b73f8b0473fd5e6'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/database.db'