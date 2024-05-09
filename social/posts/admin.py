from django.contrib import admin

# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):
    #перечисялем поля, которые должны быть отображены в админке
    list_display = ('pk', 'text', 'pub_date', 'author')
    #добавляем интерфейс по поиску постов по тексту
    search_fields = ('text',)
    #добавляем фильтр по дате
    list_filter = ('pub_date',)
    empty_value_display = "-пусто-"  # это свойство сработает для всех колонок: где пусто - там будет эта строка


admin.site.register(Post, PostAdmin)
