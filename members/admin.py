from django.contrib import admin

from .models import Member, Location

class MemberAdmin(admin.ModelAdmin):
    ordering=['category']
    list_filter = ['category']
    search_fields = ['name']

class LocationAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(Location, LocationAdmin)
