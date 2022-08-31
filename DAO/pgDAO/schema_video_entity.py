import DAO.pgDAO.connection as connection
from sqlalchemy import MetaData, Table
from sqlalchemy.ext.declarative import declarative_base


def to_dict(self):
    return {c.name.replace(self.field_prefix, ''): getattr(self, c.name, None) for c in self.__table__.columns}


Base = declarative_base(bind=connection.engine)
Base.to_dict = to_dict
metadata = MetaData(bind=connection.engine, schema='schema_video')
metadata.reflect()


class Video(Base):
    __table__ = Table('table_video', metadata, autoload=True)
    field_prefix = 'video_'


class VideoStars(Base):
    __table__ = Table('table_video_stars', metadata, autoload=True)
    field_prefix = 'video_stars_'


class VideoTags(Base):
    __table__ = Table('table_video_tags', metadata, autoload=True)
    field_prefix = 'video_tags_'
