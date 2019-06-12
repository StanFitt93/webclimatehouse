from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


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
    slug_field  = models.SlugField()
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


    