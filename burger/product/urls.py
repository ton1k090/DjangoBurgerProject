from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from .views import Index, AboutView, ContactView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]