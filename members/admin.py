from django.contrib import admin

from .models import Member, Location, Post

class MemberAdmin(admin.ModelAdmin):
    ordering=['-category']
    list_filter = ['category']
    search_fields = ['name']
    list_display = ['name', 'email', 'category']

class LocationAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
