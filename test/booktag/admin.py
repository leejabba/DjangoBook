from django.contrib import admin
from booktag.models import Booktag

# Register your models here.

class BooktagAdmin(admin.ModelAdmin):
    list_display = ('title','url')

admin.site.register(Booktag, BooktagAdmin)
