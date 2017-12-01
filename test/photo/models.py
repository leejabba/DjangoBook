from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# reverse() 함수를 사용하기 위해 임포트
from django.core.urlresolvers import reverse

# 사진에 대한 원본 이미지와 썸네일 이미지를 모두 저장할 수 있는 필드
from photo.fields import ThumbnailImageField



# Create your models here.

@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('한줄 설명', max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))


@python_2_unicode_compatible
class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length = 50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('사진 설명', blank = True)
    upload_date = models.DateTimeField('업로드 날짜', auto_now_add = True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))
