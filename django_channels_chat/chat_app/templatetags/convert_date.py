from django import template
import datetime

register = template.Library()

@register.filter(expects_localtime=True)
def convert_date(value):
    """
    Converts a string to datetime object if it is a string,
    else returns the value as is.
    """
    if isinstance(value, str):
        try:
            return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            # Fallback if microseconds are missing
            return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    return value
