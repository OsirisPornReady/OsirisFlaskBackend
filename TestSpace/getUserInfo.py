from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Integer, String, Boolean

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import mapper
from sqlalchemy.orm import Session


# echo 参数用于标记是否输出日志信息,echo=True
engine = create_engine('postgresql://postgres:123456@localhost:5432/osiris')

Base = declarative_base(bind=engine)

metadata = MetaData(bind=engine,schema='schema_user') #传给了bind参数，也能写成bind=metadata
metadata.reflect()

class User(Base):
    __table__ = Table('table_user', metadata, autoload=True)

testUser = User(id=6,user_username='fuck',user_password='fuck',user_message_count=20)

print(User)
print(testUser)
print(dir(testUser))


table_user = metadata.tables['schema_user.table_user']
table_user_authority = metadata.tables['schema_user.table_user_authority']


def select(table_class, row_id):
    session = Session(bind=engine) #传给了bind参数，也能写成bind=metadata
    try:
        return session.query(table_class).all()
    except:
        session.rollback()
    finally:
        session.close()


def insert(table_instance):
    session = Session(bind=engine)
    try:
        print(table_instance)
        session.add(table_instance)
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()





# print(metadata.tables)




def mapTable(engine):
    metadata = MetaData(bind=engine, schema='schema_user')  # 传给了bind参数，也能写成bind=metadata
    metadata.reflect()

    tableList = []
    table_user = metadata.tables['schema_user.table_user']
    table_user_authority = metadata.tables['schema_user.table_user_authority']

    tableList.append(table_user)
    tableList.append(table_user_authority)

    session = Session(bind=engine)  # 传给了bind参数，也能写成bind=metadata

    return tableList



if __name__ == '__main__':
    print(type(table_user))
    print(type(User))
    print(type(testUser))
    insert(testUser)
    result = select(table_user, 1)
    print(result)












# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'table_user'
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)
#     messageCount = Column(Integer)
#
#
# class UserAuthority(Base):
#     __tablename__ = 'table_user_authority'
#     id = Column(Integer, primary_key=True)
#     create = Column(Boolean)
#     retrieve = Column(Boolean)
#     update = Column(Boolean)
#     delete = Column(Boolean)
#
# Base.metadata.create_all()








# import psycopg2

# conn = psycopg2.connect(database="osiris", user="postgres", password="123456", host="127.0.0.1", port="5432")
#
# cursor = conn.cursor()
#
# sql = "SELECT VERSION()"
#
# cursor.execute(sql)
#
# data = cursor.fetchall()
#
# print(data)
#
# conn.commit()
#
# conn.close()
