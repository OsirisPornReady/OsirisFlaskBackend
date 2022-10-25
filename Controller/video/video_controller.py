from flask import Blueprint, request, make_response, jsonify
import Service.video.video_service as service


video_bp = Blueprint('video', __name__, url_prefix='/video')


@video_bp.route('/getAllVideo', methods=['GET'])
def getAllVideo():
    if request.method == "GET":
        print('接收到了getAllVideo请求')
        data = service.getAllVideo()
        print(data)
        return jsonify(data)


@video_bp.route('/createVideo', methods=['POST'])
def createVideo():
    if request.method == "POST":
        req_data = request.get_json()  # 此处直接处理为字典了
        print('接收到了createVideo请求:', req_data)
        vid = service.createVideo(req_data)
        if vid:
            res = make_response(jsonify(
                {
                    'id': vid
                }
            ), 200)
            print('新创建的video id:', vid)
        else:
            res = make_response('create failed', 500)
        return res


@video_bp.route('/updateVideo', methods=['POST'])
def updateVideo():
    if request.method == "POST":
        req_data = request.get_json()  # 此处直接处理为字典了
        print('接收到了updateVideo请求', req_data)
        state = service.updateVideo(req_data)
        if state:
            res = make_response(jsonify(
                {
                    'state': state
                }
            ), 200)
        else:
            res = make_response('update failed', 500)
        return res


@video_bp.route('/deleteVideo', methods=['POST'])
def deleteVideo():
    if request.method == "POST":
        req_data = request.get_json()  # 此处直接处理为字典了
        print('接收到了deleteVideo请求')
        state = service.deleteVideo(req_data)
        if state:
            res = make_response(jsonify(
                {
                    'state': state
                }
            ), 200)
        else:
            res = make_response('delete failed', 500)
        return jsonify(res)


@video_bp.route('/swapVideoOrder', methods=['POST'])
def swapVideoOrder():
    if request.method == "POST":
        req_data = request.get_json()  # 此处直接处理为字典了
        print('接收到了swapVideoOrder请求', req_data)
        state = service.swapVideoOrder(req_data)
        if state:
            res = make_response(jsonify(
                {
                    'state': state
                }
            ), 200)
        else:
            res = make_response('swap failed', 500)
        return res


if __name__ == '__main__':
    pass
