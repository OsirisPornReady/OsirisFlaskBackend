import DAO.pgDAO.connection as connection
from sqlalchemy import MetaData, Table
from sqlalchemy.ext.declarative import declarative_base


def to_dict(self):
    return {c.name: str(getattr(self, c.name, None)) for c in self.__table__.columns}


Base = declarative_base(bind=connection.engine)
Base.to_dict = to_dict
metadata = MetaData(bind=connection.engine, schema='schema_user')
metadata.reflect()


class User(Base):
    __table__ = Table('table_user', metadata, autoload=True)


class UserAuthority(Base):
    __table__ = Table('table_user_authority', metadata, autoload=True)
