from django.contrib import admin
from . import models

# Register your models here.

class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    list_filter = ('active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(models.BlogTag,BlogTagAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title','author','draft','pub_date')
    list_filter = ('draft','pub_date','published')
    list_editable = ('draft',)
    search_fields = ('tags',)
    autocomplete_fields = ('tags',)
    prepopulated_fields = {'slug' : ('blog_title',)}

admin.site.register(models.Blog,BlogAdmin)