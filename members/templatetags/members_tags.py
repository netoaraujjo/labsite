from django import template
from members.models import Member, AboutLab

register = template.Library()

@register.inclusion_tag('members/members.html')
def show_members():
    members = Member.objects.all().order_by('-category')
    return {'members': members}

@register.inclusion_tag('members/about.html')
def show_about():
    about = AboutLab.objects.get(id=1)
    return {'about': about}
