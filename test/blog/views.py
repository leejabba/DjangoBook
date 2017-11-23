from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.

# --- ListView
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2     # paginate_by 속성을 정의하는 것만으로도 장고가 제공하는 페이징 기능을 사용할 수 있다 (1페이지당 2개의 게시물)

# --- DetailView
class PostDetailView(DetailView):
    model = Post

# --- ArchiveView
class PostArchiveView(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYearArchiveView(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True     # 해당 연도에 해당하는 객체의 리스트를 만들어 템플릿에 넘겨줌. 즉 템플릿 파일에서 object_list 컨텍스트 변수를 사용할 수 있다.

class PostMonthArchiveView(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDayArchiveView(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTodayArchiveView(TodayArchiveView):
    model = Post
    date_field = 'modify_date'
