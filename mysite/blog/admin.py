from django.contrib import admin
from blog.models import Topics, Postagem, Comment

# Register your models here.

#Modelo admin do Model Comment:
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post','created_on','active')
    list_filter = ('active', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active = True)

admin.site.register(Postagem)
admin.site.register(Topics)