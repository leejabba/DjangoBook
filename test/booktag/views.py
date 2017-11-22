# 클래스형 제네릭 뷰를 임포트
from django.views.generic import ListView, DetailView
from booktag.models import Booktag

# Create your views here.

# --- ListView
class BooktagListView (ListView):
    model = Booktag

# --- DetailView
class BooktagDetailView (DetailView):
    model = Booktag

    