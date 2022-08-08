from flask import Flask
from flask_cors import CORS

from Controller.user.user_controller import user_bp  # controller导入处


app = Flask(__name__)
app.register_blueprint(user_bp)  # controller注册处
CORS(app, resources=r'/*')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
