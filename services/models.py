from django.db import models
from django.utils.safestring import mark_safe
from django.utils.timezone import now


class Service(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    paragraph   = models.TextField()
    s_img       = models.ImageField(upload_to='services/images')
    is_active   = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.s_img))

    image_tag.short_description = 'Image'