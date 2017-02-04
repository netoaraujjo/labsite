from django.contrib import admin

from .models import Member

class MemberAdmin(admin.ModelAdmin):
    ordering=['category']

# Register your models here.
admin.site.register(Member, MemberAdmin)
