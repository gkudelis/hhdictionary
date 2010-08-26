from django.template import Library, Node
from menu.models import Entry
from django.template.loader import render_to_string

register = Library()



class MenuNode(Node):
    def render(self, context):
        try:
            # Generate menu here
            menuList = Entry.objects.order_by('place')
            return render_to_string('menu.html', {
                'menuList': menuList,
            }, context_instance = context)
        except:
            return ''
        

def get_menu(parser, token):
    return MenuNode()

register.tag('get_menu', get_menu)
