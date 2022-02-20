from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    # поля которые мы хотим видеть
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    # поля которые должны быть ссылками на запись в модели
    list_display_links = ('id', 'title')
    # поля по которым адмни может проводить поиск
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    # поля которые мы хотим видеть
    list_display = ('id', 'title')
    # поля которые должны быть ссылками на запись в модели
    list_display_links = ('id', 'title')
    # поля по которым адмни может проводить поиск
    search_fields = ('title', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
