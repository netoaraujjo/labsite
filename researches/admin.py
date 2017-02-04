from django.contrib import admin

from .models import ResearchLine, Project

class ResearchLineAdmin(admin.ModelAdmin):
    search_fields = ['research_line']

class ProjectAdmin(admin.ModelAdmin):
    fields = ['project_title', 'abstract', 'research_line', 'researches']
    search_fields = ['project_title']
    list_filter = ['research_line']
# Register your models here.
admin.site.register(ResearchLine, ResearchLineAdmin)
admin.site.register(Project, ProjectAdmin)
