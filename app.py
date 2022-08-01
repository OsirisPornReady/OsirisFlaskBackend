from flask import Flask, request, jsonify
from flask_cors import CORS

from user.login import *

app = Flask(__name__)
CORS(app, resources=r'/*')

users = Users()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/user/login', methods=["POST"])
def login():
    if request.method == "POST":
        userdata = request.get_json()  # 此处直接处理为字典了
        user, state = users.validate(userdata)
        data = {
            'user': user,
            'state': state
        }
        return jsonify(data)


if __name__ == '__main__':
    app.run()
