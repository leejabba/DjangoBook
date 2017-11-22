
from django.conf.urls import url
from django.contrib import admin

# 뷰 모듈 관련 클래스 임포트
from booktag.views import BooktagListView, BooktagDetailView

# url(regex, view, kwargs=None, name=None, prefix='')
# 보통 regex(정규식), view(뷰), name(URL 패턴 이름) 인자를 사용하는 편이다.
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^booktag/$', BooktagListView.as_view(), name="index"),
    url(r'^booktag/(?P<pk>\d+)/$', BooktagDetailView.as_view(), name="detail"),
]

