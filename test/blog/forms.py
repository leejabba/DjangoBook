# 폼을 클래스로 표현할 수 있도록 하는 기능을 django.forms 모듈에서 제공한다.
from django import forms

# django.forms 모듈의 Form 클래스를 상속받아 클래스 정의
class PostSearchForm(forms.Form):
    # label -> 레이블, search_word -> 필드 ID
    search_word = forms.CharField(label='검색어 입력 ')