from django import template
from members.models import Member, AboutLab, Location

register = template.Library()

@register.inclusion_tag('members/members.html')
def show_members():
    members = Member.objects.all().order_by('-category')
    return {'members': members}

@register.inclusion_tag('members/about.html')
def show_about():
    about = AboutLab.objects.all()[:1]
    if len(about) > 0:
        about = about[0]
    return {'about': about}

@register.inclusion_tag('members/location.html')
def show_location():
    location = Location.objects.all()[:1]
    if len(location) > 0:
        location = location[0]
    return {'location': location}
