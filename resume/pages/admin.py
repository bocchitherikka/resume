from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title', 'text')
    empty_value_display = 'ТУТ ПУСТААА((('


admin.site.register(Post, PostAdmin)
