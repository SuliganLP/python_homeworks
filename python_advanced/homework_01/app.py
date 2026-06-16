from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Flask!'


@app.route('/user/<username>')
def greet_user_name(username):
    return f"Hello, {escape(username)}!"


if __name__ == '__main__':
    app.run()
