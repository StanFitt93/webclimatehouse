from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Banner, Slider


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title','is_active','ban_img_show']
    fields = ['title','is_active','ban_img','ban_img_show']
    readonly_fields = ['ban_img_show']

    def ban_img_show(self,obj):
        return mark_safe('<img src="{url}" width="300" height="300" />'.format(
            url=obj.ban_img.url,
            width=obj.ban_img.width,
            height=obj.ban_img.height,
        )
        )


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title','is_active','img_slider','slider_img_show']
    fields = ['title', 'is_active', 'img_slider', 'slider_img_show', 'description']
    readonly_fields = ['slider_img_show']

    def slider_img_show(self, obj):
        return mark_safe('<img src="{url}" width="300" height="300" />'.format(
            url=obj.img_slider.url,
            width=obj.img_slider.width,
            height=obj.img_slider.height,
        )
        )





