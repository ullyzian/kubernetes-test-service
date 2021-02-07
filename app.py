from flask import Flask
import psycopg2
import socket

conn = psycopg2.connect(dbname="database", user="user", password="password", host="10.106.41.56")

app = Flask(__name__)


@app.route('/')
def hello_world():
    with conn.cursor() as curs:
        curs.execute("SELECT version();")
        version = curs.fetchone()
    conn.close()
    return f'Hello World with Kubernetes example!' \
           f'\nIP:{socket.gethostbyname(socket.gethostname())}' \
           f'\nPostgres version: {version}'


if __name__ == '__main__':
    app.run()
