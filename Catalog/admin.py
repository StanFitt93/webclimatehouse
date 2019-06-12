from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Brand, Product
# Register your models here.


@admin.register(Brand)
class BrandAdminModel(admin.ModelAdmin):
    list_display = ['name', 'brand_img_show']
    fields = ['name', 'slug', 'brand_img', 'brand_img_show']
    readonly_fields = ['brand_img_show']

    def brand_img_show(self,obj):
        return mark_safe('<img src="{url}" width="300" height="200" />'.format(
            url=obj.brand_img.url,
            width=obj.brand_img.width,
            height=obj.brand_img.height,
        )
        )


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['title', 'category', 'brand', 'product_img', 'available', 'price', 'slug_field']
    fields = ['title',
              'category',
              'brand',
              'price',
              'product_img',
              'product_img_show',
              'available',
              'slug_field',
              'description']
    readonly_fields = ['product_img_show']

    def product_img_show(self, obj):
        return mark_safe('<img src="{url}" width="150" height="100" />'.format(
            url=obj.product_img.url,
            width=obj.product_img.width,
            height=obj.product_img.height,
        )
        )


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available_sale']
    fields = ['name', 'slug', 'available_sale']