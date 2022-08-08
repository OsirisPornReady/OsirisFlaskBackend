from sqlalchemy.orm import Session

import DAO.pgDAO.connection as connection  # from...import... 导入的是副本，且污染命名空间，要跨模块使用变量请用import方式导入
from DAO.pgDAO.entity import User, UserAuthority


def login(userdata):
    username = userdata['username']
    password = userdata['password']
    session = Session(bind=connection.engine)
    try:
        user = session.query(User).filter(User.user_username == username).first()
        if user:
            if user.user_password == password:
                print('登陆成功', user.to_dict())
                return {    # 成功登录
                            'user': user.to_dict(),
                            'state': user.id
                        }
            else:
                return {    # 密码错误
                        'user': None,
                        'state': -1
                        }
        else:
            return {    # 用户不存在
                        'user': None,
                        'state': -2
                    }
    except Exception as e:
        print('查询数据时发生异常')
        print(e)
        session.rollback()
        return {    # 发生异常
                    'user': None,
                    'state': -3
                }
    finally:
        session.close()


def register():
    session = Session(bind=connection.engine)
    try:
        new_user = User(id=7, user_username='fuck', user_password='fuck', user_message_count=20)
        session.add(new_user)
        session.commit()
        print('插入数据', new_user)
    except Exception as e:
        print('插入数据时发生异常')
        print(e)
        session.rollback()
    finally:
        session.close()


if __name__ == '__main__':
    pass
