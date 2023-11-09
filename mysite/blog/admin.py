from django.contrib import admin
from blog.models import Topics, Postagem

# Register your models here.

admin.site.register(Postagem)
admin.site.register(Topics)