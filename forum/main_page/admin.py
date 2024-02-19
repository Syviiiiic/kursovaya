from django.contrib import admin
from .models import Subject, Comment, Like, Category


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'slug', 'status')
    list_filter = ('publish', 'status', 'created', 'author')
    search_fields = ('body', 'title')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created', 'active')
    list_filter = ('name', 'created', 'updated', 'active')
    search_fields = ['name', 'subject', 'body']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'value',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)