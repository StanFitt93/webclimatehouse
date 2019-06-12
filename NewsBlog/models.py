from __future__ import unicode_literals
from future.types.newstr import unicode
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.db.models.signals import pre_save
from transliterate import translit
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

def pre_save_category_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        slug = slugify(translit(unicode(instance.title),reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=Category)


class News(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    paragraph = models.TextField()
    img_news = models.ImageField(upload_to='news/images')
    is_active = models.BooleanField(default=False)
    date_news = models.DateTimeField(default=now)
    slug_field = models.SlugField(blank=True,unique=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.img_news))

    image_tag.short_description = 'Image'


def pre_save_news_slug(sender,instance,*args,**kwargs):
    if not instance.slug_field:
        slug_field = slugify(translit(unicode(instance.title),reversed=True))
        instance.slug_field = slug_field


pre_save.connect(pre_save_news_slug,News)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    paragraph = models.TextField()
    img_blog = models.ImageField(upload_to='blog/images')
    is_active = models.BooleanField(default=False)
    date_blog = models.DateTimeField(default=now)
    slug_field = models.SlugField(blank=True,unique=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.img_blog))

    image_tag.short_description = 'Image'


def pre_save_blog_slug(sender,intance,*args,**kwargs):
    if not intance.slug_field:
        slug_field = slugify(translit(unicode(intance.title), reversed=True))
        intance.slug_field = slug_field

pre_save.connect(pre_save_blog_slug, sender=Blog)
