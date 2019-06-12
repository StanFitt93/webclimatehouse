from django.contrib import admin
from .models import Service
from django.utils.safestring import mark_safe


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'ser_img_show', 'slug']
    fields = ['title', 'is_active', 'description','s_img', 'ser_img_show','paragraph', 'slug']
    readonly_fields = ['ser_img_show']

    def ser_img_show(self, obj):
        return mark_safe('<img src="{url}" width="300" height="300" />'.format(
            url=obj.s_img.url,
            width=obj.s_img.width,
            height=obj.s_img.height,
        )
        )
