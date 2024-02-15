from flask import Flask, send_from_directory, render_template

app = Flask(__name__)


@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)


@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title=title)


@app.route('/')
def root():
    return render_template("base.html", title="Default")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
