from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)


@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    lista_display = ('title')
