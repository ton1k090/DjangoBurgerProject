from django.urls import path

from blog.views import BlogListView, BlogDetailView, PostByCategory, add_comment

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='post_detail'),
    path('category/<int:pk>', PostByCategory.as_view(), name='category_list' ),
    path('add_comment/<slug:slug>/', add_comment, name='add_comment'),

]