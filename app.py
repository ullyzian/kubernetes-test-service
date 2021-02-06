from flask import Flask
import socket

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'Hello World!\nIP: {socket.gethostbyname(socket.gethostname())}'


if __name__ == '__main__':
    app.run()
