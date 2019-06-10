from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Banner


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








