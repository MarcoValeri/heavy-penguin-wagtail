from django.utils.html import format_html
from django.templatetags.static import static

from wagtail.core import hooks

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import BlogPage

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('wagtail/theme.css'))

class BlogPageAdmin(ModelAdmin):
    model = BlogPage
    menu_label = "Post"
    menu_icon = "help"
    menu_order = 200
    

modeladmin_register(BlogPageAdmin)