from django.contrib import admin

from .models import Article, Comment


class CommantInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommantInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
