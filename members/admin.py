from django.contrib import admin
from .models import main_model,blog_post
# Register your models here.
admin.site.register(main_model)
admin.site.register(blog_post)