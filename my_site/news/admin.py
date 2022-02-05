from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    # поля которые мы хотим видеть
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    # поля которые должны быть ссылками на запись в модели
    list_display_links = ('id', 'title')
    # поля по которым адмни может проводить поиск
    search_fields = ('title', 'content')


admin.site.register(News, NewsAdmin)
