from django.contrib import admin

from .models import Comment, Group, Post


class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_display = ('pk', 'text', 'pub_date', 'author')
    list_filter = ('pub_date',)
    search_fields = ('text',)


admin.site.register(Comment)
admin.site.register(Group)
admin.site.register(Post, PostAdmin)
