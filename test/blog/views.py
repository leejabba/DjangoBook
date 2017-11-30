from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q  # 검색 기능에 필요한 Q 클래스 임포트
from django.shortcuts import render     # 단축함수 render()를 임포트

from blog.models import Post

# Create your views here.


# --- TemplateView
class TagTemplateView (TemplateView):
    template_name = 'tagging/tagging_cloud.html'

# --- ListView
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2     # paginate_by 속성을 정의하는 것만으로도 장고가 제공하는 페이징 기능을 사용할 수 있다 (1페이지당 2개의 게시물)

class PostTaggedObjectList(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'

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


# --- FormView
# Post 요청을 받게 되면 FormView 클래스에서 데이터 유효성을 체크 한 후 form_valid() 함수를 실행하고
# 적절한 URL로 리다이렉트 시킨다.
#  > Get 요청 : 폼을 화면에 보여주고 사용자의 입력을 기다림
#  > Post 요청 : 사용자가 폼에 데이터 입력후 제출함
class SearchFormView(FormView):
    form_class = PostSearchForm     # 폼으로 사용될 클래스 지정
    template_name = 'blog/post_search.html'

    def form_valid(self, format):
        schWord = '%s' % self.request.POST['search_word']   # POST 요청의 search_word 파라미터 값을 추출
        # Q 객체로 filter() 메소드의 매칭 조건을 다양하게 설정
        # icontains: 대소문자 구분하지 않고 단어 포함 조사
        # distinct(): 중복된 객체 제외
        post_list = Post.objects.filter(Q(title__icontains=schWord)|Q(description__icontains=schWord)|Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = format
        context['search_term'] = schWord
        context['object_list'] = post_list

        # render()는 템플릿 파일과 컨텍스트 변수를 처리해, 최종적으로 HttpResponse 객체를 반환한다.
        # form_valid() 함수는 보통 리다이렉트 처리를 위해 HttpResponse 객체를 반환하는데,
        # render() 함수에 의해 리다이렉트 처리가 되지 않는다. 
        return render(self.request, self.template_name, context)