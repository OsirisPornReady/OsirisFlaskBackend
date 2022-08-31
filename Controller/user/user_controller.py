from flask import Blueprint, request, make_response, jsonify
import Service.user.user_service as service
from flask_siwadoc import SiwaDoc


user_bp = Blueprint('user', __name__, url_prefix='/user')  # 在蓝本对象的名称后添加一个_bp后缀（即blueprint的简写）并不是必须的，这里是为了更容易区分蓝本对象，而且可以避免潜在的命名冲突。
# print('[Controller/user/user_controller]: user蓝图已加载')


@user_bp.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        userdata = request.get_json()  # 此处直接处理为字典了
        res = service.login(userdata)
        try:
            print(res)
            return jsonify(res)
        except Exception as e:
            print('序列化失败')
            print(e)
            error = {
                'user': None,
                'state': -3
            }
            return jsonify(error)


@user_bp.route('/register', methods=['GET'])
def register():
    service.register()
    return '添加了一行数据'


@user_bp.route('/test', methods=['GET'])
def test():
    return 'userTest'


@user_bp.route('/getUserInfo', methods=['GET'])
def getUserInfo():
    service.get_user_info()
    return 'get user info'


@user_bp.route('/setCookie', methods=['GET'])
def setCookie():
    res = make_response()
    res.set_cookie('somecookiename', 'I am cookie')
    return res


@user_bp.route('/getCookie', methods=['GET'])
def getCookie():
    pass


if __name__ == '__main__':
    pass
