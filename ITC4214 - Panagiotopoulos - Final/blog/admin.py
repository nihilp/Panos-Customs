from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


@admin.register(models.Motorcycles)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(models.Category)
admin.site.register(models.ProductionCompany)
admin.site.register(models.PanosCustoms)
admin.site.register(models.Comment, MPTTModelAdmin)
