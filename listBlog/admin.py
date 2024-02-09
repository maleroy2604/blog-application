from django.contrib import admin

from listBlog.bloform import BlogForm
from listBlog.models import Blog, ImageUrl, Content, Title, Comment, Category
from listBlog.contentform import ContentForm


class ContentAdmin(admin.ModelAdmin):
    form = ContentForm


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm


admin.site.register(Blog)
admin.site.register(ImageUrl)
admin.site.register(Content, ContentAdmin)
admin.site.register(Title)
admin.site.register(Comment)
admin.site.register(Category)
