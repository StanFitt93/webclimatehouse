from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from future.types.newstr import unicode
from transliterate import translit


class TypeOfSaleProduct(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Тип продажи'
        verbose_name_plural = 'Типы продаж'

    def __str__(self):
        return self.title


class CategoryManager(models.Manager):
    def all(self,*args,**kwargs):
        return super(CategoryManager, self).get_queryset().filter(available=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    available = models.BooleanField(default=False)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


def pre_save_category_slug(sender, instance, *args, **kwargs):
    slug = slugify(translit(unicode(instance.name), reversed=True))
    instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=Category)


class SubcategoryManager(models.Manager):
    def all(self,*args,**kwargs):
        return super(SubcategoryManager, self).get_queryset().filter(available=True)


class Subcategory(models.Model):
    title = models.CharField(max_length=200)
    available = models.BooleanField(default=False)
    objects = SubcategoryManager()
    main = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return  self.title







class BrandManager(models.Manager):
    def all(self,*args,**kwargs):
        return super(BrandManager, self).get_queryset().filter(available=True)


class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    brand_img = models.ImageField(upload_to='catalog/brands/images')
    available = BrandManager()

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.brand_img))

    image_tag.short_description = 'Image'


class ProductManager(models.Manager):
    def all(self,*args,**kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    
    brand       = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    title       = models.CharField(max_length=200)
    slug_field  = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    product_img = models.ImageField(upload_to='catalog/products/images')
    price       = models.DecimalField(max_digits=9,decimal_places=2)
    available   = models.BooleanField(default=False)
    objects     = ProductManager()
    typeOfSale  = models.ForeignKey(TypeOfSaleProduct, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name= 'Товар'
        verbose_name_plural= 'Товары'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="100" />' % (self.product_img))

    image_tag.short_description = 'Image'


def pre_save_slug_product(sender,instance,*args,**kwargs):
       slug = slugify(translit(unicode(instance.title), reversed=True))
       instance.slug_field = slug


pre_save.connect(pre_save_slug_product,Product)
