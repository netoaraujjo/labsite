from django import template
from members.models import Member

register = template.Library()

@register.inclusion_tag('members/members.html')
def show_members():
    members = Member.objects.all().order_by('-category')
    return {'members': members}
