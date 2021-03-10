from my_server import socketio, app

if __name__ == '__main__':
    socketio.run(app, host='localhost', port='8000', debug=True)