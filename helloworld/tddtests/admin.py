from django.contrib import admin
from .models import Sentiments


class SentimentsAdmin(admin.ModelAdmin):
    list_display = ['word', 'goodbad']
    list_filter = ['date']
    search_fields = ['word']

admin.site.register(Sentiments,SentimentsAdmin)
