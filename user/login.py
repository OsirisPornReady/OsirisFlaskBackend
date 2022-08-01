import json

# Users = {}

# def initUsers():
#     f = open('../users.json','r')
#     users = json.load(f)
#     return users
#
# def validate(user):
#     pass


class Users:
    def __init__(self):
        f = open('users.json', 'r') #该文件作为模块在其他文件中调用时，相对路径是相对于调用的文件而言的
        self.users = json.load(f)

    def validate(self,userdata): #外部直接处理为字典，可以直接用
        username = userdata['username']
        password = userdata['password']
        for index,user in enumerate(self.users): #匹配用户名和密码就返回
            if user['username'] == username:
                if user['password'] == password:
                    return user,index                 #成功登录
                else:
                    return None,-1                    #密码错误
        return None,-2                              #用户不存在


if __name__ == '__main__':
    # Users = initUsers()
    pass

