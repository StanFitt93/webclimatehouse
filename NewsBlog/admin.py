from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category,News,Blog

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['date_news','title','category','news_img_show','is_active']
    fields = ['title','category','description','paragraph','img_news','is_active','date_news']
    readonly_fields = ['news_img_show']

    def news_img_show(self,obj):
        return mark_safe('<img src="{url}" width="300" height="300" />'.format(
            url=obj.img_news.url,
            width=obj.img_news.width,
            height=obj.img_news.height,
        )
        )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['date_blog','title','category','is_active','blog_img_show']
    fields = ['title','category','description','paragraph','img_blog','is_active','date_blog']
    readonly_fields = ['blog_img_show']

    def blog_img_show(self,obj):
        return mark_safe('<img src="{url}" width="300" height="300" />'.format(
            url=obj.img_blog.url,
            width=obj.img_blog.width,
            height=obj.img_blog.height,
        )
        )