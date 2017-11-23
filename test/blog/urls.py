from django.conf.urls import url
from blog.views import *

urlpatterns = [

    # /
    url(r'^$', PostListView.as_view(), name='index'),

    # /post/
    url(r'^post/$', PostListView.as_view(), name='post_list'),

    # /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_detail'),

    # /archive/
    url(r'^archive/$', PostArchiveView.as_view(), name='post_archive'),

    # /2012/
    url(r'^(?P<year>\d{4})/$', PostYearArchiveView.as_view(), name='post_year_archive'),

    # /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMonthArchiveView.as_view(), name='post_month_archive'),

    # /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDayArchiveView.as_view(), name='post_day_archive'),

    # /today/
    url(r'^today/$', PostTodayArchiveView.as_view(), name='post_today_archive'),
]