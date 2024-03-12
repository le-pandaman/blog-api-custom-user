from django.contrib import admin

from .models import Posts
# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'created_at', 'author']
    list_display_links = ['title', 'created_at', 'author']
    search_fields = ('title', 'author__username',)
    fieldsets = ((None, {'fields': ('title', 'body', 'author',)}),)


admin.site.register(Posts, PostAdmin)
