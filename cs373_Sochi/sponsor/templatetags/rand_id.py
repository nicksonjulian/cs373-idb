from django import template
import random
register = template.Library()

def rand_id(num):
    r = random.randint(1,num)
    return str(r)

register.filter('rand_id', rand_id)