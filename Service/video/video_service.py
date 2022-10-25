from sqlalchemy.orm import Session

import DAO.pgDAO.connection as connection  # from...import... 导入的是副本，且污染命名空间，要跨模块使用变量请用import方式导入
from DAO.pgDAO.schema_video_entity import Video, VideoStars, VideoTags

from utility.converter import convert_video_2_dto


# ---------------------------session装饰器--------------------------------
def SessionDecorator(func):  # 手动控制commit,有时候可能要commit之后才能拿到id
    def wrapper(*args, **kw):
        session = Session(bind=connection.engine)
        kw['session'] = session
        try:
            result = func(*args, **kw)  # 包装后必须要有一个变量接住内部函数运行的结果，不管有没有返回值
            return result
        except Exception as e:
            print('修改视频数据时发生异常')
            print(e)
            session.rollback()
            return False
        finally:  # 会在try中的return之前执行,如果finally中也有return,则finally中的return先执行
            session.close()
    return wrapper
# ------------------------------------------------------------------


@SessionDecorator
def getAllVideo(**kw):
    session = kw['session']

    videoList = []
    videos = session.query(Video).all()
    for video in videos:
        stars = [star[0] for star in session.query(VideoStars.star).filter(VideoStars.video_id == video.id).all()]
        tags = [tag[0] for tag in session.query(VideoTags.tag).filter(VideoTags.video_id == video.id).all()]
        videoList.append(convert_video_2_dto(video, stars, tags))

    return videoList


@SessionDecorator
def createVideo(data, **kw):
    session = kw['session']

    video = data['video']
    new_video = Video(video_title=video['title'], video_thumbnail=video['thumbnail'], video_path=video['path'])
    session.add(new_video)
    session.commit()
    for star in video['stars']:
        new_star = VideoStars(video_id=new_video.id, star=star)
        session.add(new_star)
    for tag in video['tags']:
        new_tag = VideoTags(video_id=new_video.id, tag=tag)
        session.add(new_tag)
    session.commit()

    return new_video.id


@SessionDecorator
def updateVideo(data, **kw):
    session = kw['session']

    # 获取id, video
    vid = data['id']
    video = data['video']

    # 更新video表
    query_video = session.query(Video).filter(Video.id == vid).first()
    query_video.video_title = video['title']
    query_video.thumbnail = video['thumbnail']
    query_video.path = video['path']

    # 删除stars和tags表中的对应数据(直接全更新,无需比对,比对反而效率更低),插入新数据
    session.query(VideoStars).filter(VideoStars.video_id == vid).delete()
    session.query(VideoTags).filter(VideoTags.video_id == vid).delete()
    for star in video['stars']:
        new_star = VideoStars(video_id=vid, star=star)
        session.add(new_star)
    for tag in video['tags']:
        new_tag = VideoTags(video_id=vid, tag=tag)
        session.add(new_tag)

    session.commit()
    return True


@SessionDecorator
def deleteVideo(data, **kw):
    session = kw['session']

    vid = data['id']
    session.query(Video).filter(Video.id == vid).first().delete()
    session.query(VideoStars).filter(VideoStars.video_id == vid).delete()
    session.query(VideoTags).filter(VideoTags.video_id == vid).delete()

    session.commit()
    return True


@SessionDecorator
def swapVideoOrder(data, **kw):
    session = kw['session']

    pid = data['pid']
    cid = data['cid']
    query_video_p = session.query(Video).filter(Video.id == pid).first()
    query_video_c = session.query(Video).filter(Video.id == cid).first()

    pOrder = query_video_p.video_order
    cOrder = query_video_c.video_order

    query_video_p.video_order = cOrder
    query_video_c.video_order = pOrder

    session.commit()
    return True


if __name__ == '__main__':
    pass
