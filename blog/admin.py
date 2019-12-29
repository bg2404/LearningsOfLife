from django.contrib import admin
from .models import Blog, Comment
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title', )}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
