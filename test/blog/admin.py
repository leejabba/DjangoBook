from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','description','modify_date')      
    list_filter = ('modify_date',)              # modify_date 컬럼을 사용하는 필터 사이드바
    search_fields = ('title', 'content')        # 검색박스 표시, title과 content 컬럼에서 키워드 검색
    prepopulated_fields = {'slug':('title',)}   # slug 필드는 title 필드를 사용해 미리 채워지도록 함

admin.site.register(Post, PostAdmin)            # admin.site.register() 함수를 사용해 Post와 PostAdmin 클래스를 Admin 사이트에 등록
