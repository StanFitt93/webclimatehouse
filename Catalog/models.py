from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from future.types.newstr import unicode
from transliterate import translit


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,unique=True)
    available_sale = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(unicode(instance.name), reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=Category)


class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    brand_img = models.ImageField(upload_to='catalog/brands/images')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.brand_img))

    image_tag.short_description = 'Image'


class Product(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    brand       = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    title       = models.CharField(max_length=200)
    slug_field  = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    product_img = models.ImageField(upload_to='catalog/products/images')
    price       = models.DecimalField(max_digits=9,decimal_places=2)
    available   = models.BooleanField(default=False)

    class Meta:
        verbose_name= 'Товар'
        verbose_name_plural= 'Товары'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="100" />' % (self.product_img))

    image_tag.short_description = 'Image'


def pre_save_slug_product(sender,instance,*args,**kwargs):
    if not instance.slug_field:
        slug = slugify(translit(unicode(instance.title), reversed=True))
        instance.slug_field = slug


pre_save.connect(pre_save_slug_product,Product)
