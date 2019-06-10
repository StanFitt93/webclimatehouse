from django.db import models
from django.utils.safestring import mark_safe


class Banner(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    ban_img = models.ImageField(upload_to='banners/images',null=True,blank=True)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.ban_img))

    image_tag.short_description = 'Image'