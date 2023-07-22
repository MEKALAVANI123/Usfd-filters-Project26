from django import template

register = template.Library()

@register.filter('swapping')
def swap(data):
    return data.swapcase()

@register.filter()
def remove(data,arg):
    return data.replace(arg,'')

@register.filter()
def counting(S,sub):
    c=0
    for i in range(len(S)):
        if S[i:i+len(sub):]==sub:
            c+=1
    return c
