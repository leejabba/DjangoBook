from django.conf.urls import url
from photo.views import *

urlpatterns = [
    # /
    url(r'^$', AlbumListView.as_view(), name='index'),

    # /album/, same as /
    url(r'^album/$', AlbumListView.as_view(), name='album_list'),

    # /album/99/
    url(r'^album/(?P<pk>\d+)/$', AlbumDetailView.as_view(), name='album_detail'),

    # /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo_detail'),
]