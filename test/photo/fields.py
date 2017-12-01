# ImageField, ImageFieldFile 클래스 임포트 (장고 기본 필드)
from django.db.models.fields.files import ImageField, ImageFieldFile

# 6장에서 설치한 파이썬 이미지 처리 라이블러리 PIL.Image 임포트
from PIL import Image

import os

# 기존 이미지 파일명을 기준으로 썸네일 이미지 파일명을 만드는 함수
def _add_thumb(s):
    parts = s.split(".")
    parts.insert(-1, "thumb")

    # 이미지의 확장자가 jepg 또는 jpg가 아닌경우 강제로 확장자명을 변경함 
    if parts[-1].lower() not in ['jepg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)

class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save = True):
        # 부모 ImageFieldFile 클래스의 save() 메소드를 호출해 원본 이미지 저장
        super(ThumbnailImageFieldFile, self).save(name, content, save)

        # 이미지를 img 변수에 담아 썸네일을 생성한다.
        img = Image.open(self.path)
        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))    # 백그라운드 이미지 생성
        # 썸네일과 백그라운드 이미지를 합쳐서 정사각형 모양의 썸네일 이미지를 만든다.
        background.paste(img, ( int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2) ))
        background.save(self.thumb_path, 'JPEG')

    # delete() 메소드 호출시 원본 이미지와 썸네일 이미지 모두 삭제되는 로직
    def delete(self, save = True):
        if os.paht.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)

# 장고 모델 정의에 사용하는 필드 역할을 하는 클래스
class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_hight=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_hight
        super(ThumbnailImageField, self).__init__(*args, **kwargs)

