from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Gallery, Contact, About, Social, Reviews, BestBurger


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'get_image')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'description', 'price')
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110" ')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110" ')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'phone')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="110" ')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="110" ')


@admin.register(BestBurger)
class BestBurgerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110" ')