from django import template
register = template.Library()

def html_string(url_str):

    url_str = url_str.replace (" ", "_").lower().replace("'", "").replace(".", "")
    return url_str

register.filter('stringify', html_string)