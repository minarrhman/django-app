from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published', 'realtor', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    list_editable = ('is_published',)
    search_fields = ('title', 'price')
    list_per_page = 30
admin.site.register(Listing, ListingAdmin)

