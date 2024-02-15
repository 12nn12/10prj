from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)


@app.route('/index/<title:title>')
def index(title):
    pass

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
