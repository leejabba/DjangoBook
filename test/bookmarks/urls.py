from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# 뷰 모듈 관련 클래스 임포트
from booktag.views import BooktagListView, BooktagDetailView
from bookmarks.views import HomeView

# url(regex, view, kwargs=None, name=None, prefix='')
# 보통 regex(정규식), view(뷰), name(URL 패턴 이름) 인자를 사용하는 편이다.
urlpatterns = [
    # /
    url(r'^$', HomeView.as_view(), name="home"),

    # /admin/
    url(r'^admin/', admin.site.urls),   

    # /booktag/
    url(r'^booktag/', include('booktag.urls', namespace='booktag')),

    # /blog/
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # # /photo/
    url(r'^photo/', include('photo.urls', namespace='photo')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

