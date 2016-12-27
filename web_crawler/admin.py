from django.contrib import admin
from .models import Risk_map_article
# Register your models here.

@admin.register(Risk_map_article)
class web_crawlerAdmin(admin.ModelAdmin):
    list_display = ['hashcode','title','content','year','month','day','time','reporter']
