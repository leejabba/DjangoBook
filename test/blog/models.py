from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
# reverse() 함수를 사용하기 위해 임포트
from django.core.urlresolvers import reverse
# tagging를 사용하기 위한 임포트
from tagging.fields import TagField

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    # allow_unicode=True 는 한글 처리를 가능하게 한다.
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.abs')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    tag = TagField()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)    # 모델 객체의 리스트 출력시 modify_date 컬럼을 기준으로 내림차순으로 정렬한다.

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        # reverse() 함수는 URL 패턴을 만들어주는 장고의 내장함수이다.
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()

