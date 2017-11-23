from django.conf.urls import url
from booktag.views import BooktagListView, BooktagDetailView

urlpatterns = [
    # Class-based views
    # URL 패턴 이름:: booktag:index
    url(r'^$', BooktagListView.as_view(), name='index'),
    # URL 패턴 이름:: booktag:detail
    url(r'^(?P<pk>\d+)/$', BooktagDetailView.as_view(), name='detail')
]