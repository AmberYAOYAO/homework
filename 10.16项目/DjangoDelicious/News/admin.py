from django.contrib import admin
from News.models import *
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ["title","description","time"]
    list_filter = ["title"]
admin.site.register(News,NewsAdmin)
admin.site.register(NewsType)
admin.site.register(Editor)

