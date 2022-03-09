from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    content = models.TextField('Контент', blank=True)
    created_at = models.DateTimeField('Дата публ.', auto_now_add=True)
    edited_at = models.DateTimeField('Дата посл. ред.', auto_now=True)
    image = models.ImageField('Картинка', upload_to="photos/%Y/%m/%d", blank=True)
    is_published = models.BooleanField('Опубликовано ?', default=True)
    category = models.ManyToManyField('Category', blank=True, related_name='news')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']