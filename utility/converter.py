# 虽说是dto,但其实是字典

def convert_user_2_dto(user, authority, state=None):  # 传入对象,返回字典
    if user and authority and not state:
        user = user.to_dict()
        authority = authority.to_dict()

        user_id = user.pop('id')
        authority.pop('id')
        user['authority'] = authority

        dto = {
            'user': user,
            'state': user_id
        }
        return dto
    else:
        dto = {
            'user': None,
            'state': state
        }
        return dto


def convert_video_2_dto(video, stars, tags):
    video = video.to_dict()
    video['stars'] = stars
    video['tags'] = tags
    return video


if __name__ == '__main__':
    pass
