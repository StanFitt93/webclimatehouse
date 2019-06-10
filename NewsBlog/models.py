from django.db import models
from django.utils.safestring import mark_safe
from django.utils.timezone import now


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    paragraph = models.TextField()
    img_news = models.ImageField(upload_to='news/images')
    is_active = models.BooleanField(default=False)
    date_news = models.DateTimeField(default=now)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.img_news))

    image_tag.short_description = 'Image'


class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    paragraph = models.TextField()
    img_blog = models.ImageField(upload_to='blog/images')
    is_active = models.BooleanField(default=False)
    date_blog = models.DateTimeField(default=now)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.img_blog))

    image_tag.short_description = 'Image'
