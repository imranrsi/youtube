from django import template

register=template.Library()

@register.filter(name="mysupercut")
def mycut(value,args):
    """

    this is custom filter to cut arg..
    """

    value=value.replace(args,"")

    return value


# register.filter('mysupercut',mycut)

@register.filter(name="addstring")

def Add(value,args):

    value=value+args

    return value
