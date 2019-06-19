from django.contrib import admin

from .models import Glass

class GlassAdmin(admin.ModelAdmin):
    list_display = ['name_glass','price','quntity']
    fieldsets = [
        (None, {'fields': ['name_glass']}),
        ('Date information', {
            'fields': ['price','quntity','date'], 
            
        }),
    ]
    list_filter = ['date']
    search_fields = ['name_glass']

admin.site.register(Glass, GlassAdmin)
