from django import template
from researches.models import ResearchLine

register = template.Library()

@register.inclusion_tag('researches/research_lines.html')
def show_research_lines():
    research_lines = ResearchLine.objects.all().order_by('research_line')
    return {'research_lines': research_lines}
