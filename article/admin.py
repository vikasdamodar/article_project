from django.contrib import admin

from article.models import BlogArticle


@admin.register(BlogArticle)
class BlogArticleModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'is_published']
    readonly_fields = ('slug', )
