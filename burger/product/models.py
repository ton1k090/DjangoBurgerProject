from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class BestBurger(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='best_products/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Бургер месяца'
        verbose_name_plural = 'Бургеры месяцы'


class Gallery(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='gallery/', verbose_name='Картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлереи'


class Contact(models.Model):
    city = models.CharField(max_length=150, verbose_name='Город')
    address = models.CharField(max_length=150, verbose_name='Адресс')
    phone = models.CharField(max_length=150, verbose_name='Телефон')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class About(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Social(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='social/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = 'Социальные сети'


class Reviews(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    text = models.TextField(verbose_name='Текст отзыва')
    photo = models.ImageField(upload_to='reviews/', verbose_name='Аватарка')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'