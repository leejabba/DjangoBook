from django.contrib import admin
from photo.models import Album, Photo

# Register your models here.

# ForeignKey로 연결된 테이블을 같이 보여주는 형식 정의
#  > StackedInline: 세로로 나열되는 형식
#  > TabularInline: 테이블 모양처럼 행으로 나열되는 형식
class PhotoInline(admin.TabularInline):
    model = Photo   # 추가로 보여주는 테이블은 Photo 테이블임
    extra = 2       # 이미 입력된 객체 외에 추가로 입력할 수 있는 Photo 테이블 객체의 수는 2개임

class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]     # 앨범 객체를 보여줄 때 PhotoInline 클래스에서 정의한 사항을 함께 보여줌
    list_display = ('name','description')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title','upload_date')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)