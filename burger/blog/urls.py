from django.urls import path

from blog.views import BlogListView, AboutView, ContactView

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact')
]