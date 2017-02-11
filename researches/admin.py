from django.contrib import admin

from .models import ResearchLine, Publication

class ResearchLineAdmin(admin.ModelAdmin):
    search_fields = ['research_line']

class PublicationAdmin(admin.ModelAdmin):
    search_fields = ['project_title']
    list_filter = ['authors']

# Register your models here.
admin.site.register(ResearchLine, ResearchLineAdmin)
admin.site.register(Publication, PublicationAdmin)
