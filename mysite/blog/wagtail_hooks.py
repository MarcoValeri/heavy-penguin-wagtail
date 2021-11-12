from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import BlogPage

class BlogPageAdmin(ModelAdmin):
    model = BlogPage
    menu_label = "Post"
    menu_icon = "help"
    menu_order = 200
    

modeladmin_register(BlogPageAdmin)