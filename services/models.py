from __future__ import unicode_literals
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.db.models.signals import pre_save
from transliterate import translit
from django.utils.text import slugify
from future.types.newstr import unicode


class Service(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    paragraph   = models.TextField()
    s_img       = models.ImageField(upload_to='services/images')
    is_active   = models.BooleanField(default=False)
    slug        = models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.s_img))

    image_tag.short_description = 'Image'


def pre_save_service_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        slug_f = slugify(translit(unicode(instance.title),reversed=True))
        instance.slug = slug_f


pre_save.connect(pre_save_service_slug,Service)
