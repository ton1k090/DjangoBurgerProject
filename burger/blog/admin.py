from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Post, Comment, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'category', 'is_published', 'created_at', 'get_image')
    list_filter = ('is_published', 'category', 'created_at')
    search_fields = ('title', 'text', 'created_at')
    list_editable = ('is_published',)
    list_display_links = ('title',)
    prepopulated_fields = {"slug": ("title",)}


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110" ')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'text')
    readonly_fields = ('name', 'text', 'created_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')