from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def auth_url(user, authenticated_url_name, login_url_name='login'):
    if user.is_authenticated:
        return reverse(authenticated_url_name)
    return reverse(login_url_name)