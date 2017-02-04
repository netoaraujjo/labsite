from django.contrib import admin

from .models import Member

class MemberAdmin(admin.ModelAdmin):
    ordering=['category']
    list_filter = ['category']
    search_fields = ['name']

# Register your models here.
admin.site.register(Member, MemberAdmin)
