from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'image_show','name',  'price', 'available', 'new')
    list_display_links = ['name']
    list_filter = ['available', 'new','category']
    list_editable = ('price', 'available', 'new')
    prepopulated_fields = {'slug':('name', )}


    def image_show(self,obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"

