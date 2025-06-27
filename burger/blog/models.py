from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField('Изображение', upload_to='blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='posts')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'


class Tag(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'
