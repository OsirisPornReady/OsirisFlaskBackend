from sqlalchemy.orm import Session

import DAO.pgDAO.connection as connection  # from...import... 导入的是副本，且污染命名空间，要跨模块使用变量请用import方式导入
from DAO.pgDAO.schema_user_entity import User, UserAuthority

from utility.converter import convert_user_2_dto


# ---------------------------两种装饰器--------------------------------
def select_decorator(func):
    def wrapper(*args, **kw):
        session = Session(bind=connection.engine)
        kw['session'] = session
        try:
            result = func(*args, **kw)  # 包装后必须要有一个变量接住内部函数运行的结果，不管有没有返回值
            return result
        except Exception as e:
            print('查询数据时发生异常')
            print(e)
            session.rollback()
        finally:
            session.close()
    return wrapper


def commit_decorator(func):
    def wrapper(*args, **kw):
        session = Session(bind=connection.engine)
        kw['session'] = session
        try:
            result = func(*args, **kw)  # 包装后必须要有一个变量接住内部函数运行的结果，不管有没有返回值
            session.commit()
            return result
        except Exception as e:
            print('修改数据时发生异常')
            print(e)
            session.rollback()
        finally:
            session.close()
    return wrapper
# ------------------------------------------------------------------


@select_decorator
def login(userdata, **kw):
    session = kw['session']

    username = userdata['username']
    password = userdata['password']
    user, authority = session.query(User, UserAuthority).join(UserAuthority).filter(User.user_username == username).first()
    if user:
        if user.user_password == password:
            return convert_user_2_dto(user, authority)  # 成功登录
        else:
            return convert_user_2_dto(None, None, -1)  # 密码错误
    else:
        return convert_user_2_dto(None, None, -2)  # 用户不存在


@commit_decorator
def register(**kw):
    session = kw['session']

    new_user = User(id=7, user_username='fuck', user_password='fuck', user_message_count=20)
    session.add(new_user)
    print('插入数据', new_user)


@select_decorator
def get_user_info(**kw):
    session = kw['session']

    user, authority = session.query(User, UserAuthority).join(UserAuthority).filter(User.id == 2).first()
    user = user.to_dict()
    authority = authority.to_dict()
    print(user)
    print(authority)


@select_decorator
def func1(**kw):
    session = kw['session']


@commit_decorator
def func2(**kw):
    session = kw['session']


# -------------------------
# session = Session(bind=connection.engine)
# try:
#
#     session.commit()
# except Exception as e:
#     print(' 数据时发生异常')
#     print(e)
#     session.rollback()
# finally:
#     session.close()
# -------------------------


# def login(userdata):
#     username = userdata['username']
#     password = userdata['password']
#     session = Session(bind=connection.engine)
#     try:
#         user = session.query(User).filter(User.user_username == username).first()
#         if user:
#             if user.user_password == password:
#                 print('登陆成功', user.to_dict())
#                 return {    # 成功登录
#                             'user': user.to_dict(),
#                             'state': user.id
#                         }
#             else:
#                 return {    # 密码错误
#                         'user': None,
#                         'state': -1
#                         }
#         else:
#             return {    # 用户不存在
#                         'user': None,
#                         'state': -2
#                     }
#     except Exception as e:
#         print('查询数据时发生异常')
#         print(e)
#         session.rollback()
#         return {    # 发生异常
#                     'user': None,
#                     'state': -3
#                 }
#     finally:
#         session.close()
#
#
# def register():
#     session = Session(bind=connection.engine)
#     try:
#         new_user = User(id=7, user_username='fuck', user_password='fuck', user_message_count=20)
#         session.add(new_user)
#         session.commit()
#         print('插入数据', new_user)
#     except Exception as e:
#         print('插入数据时发生异常')
#         print(e)
#         session.rollback()
#     finally:
#         session.close()
#
#
# def getUserInfo():
#     session = Session(bind=connection.engine)
#     try:
#         user, authority = session.query(User, UserAuthority).join(UserAuthority).filter(User.id == 2).first()
#         user = user.to_dict()
#         authority = authority.to_dict()
#         print(user)
#         print(authority)
#         session.commit()
#     except Exception as e:
#         print(' 数据时发生异常')
#         print(e)
#         session.rollback()
#     finally:
#         session.close()
#
#
# @selectDecorator
# def decoTest(**kw):
#     session = kw['session']
#     user, authority = session.query(User, UserAuthority).join(UserAuthority).filter(User.id == 2).first()
#     user = user.to_dict()
#     authority = authority.to_dict()
#     print(user)
#     print(authority)


if __name__ == '__main__':
    pass
