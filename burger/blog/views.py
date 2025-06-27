from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView

from blog.forms import CommentForm
from blog.models import Post, Category, Comment


class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_page.html'

    def get_context_data(self, **kwargs):
        '''Для динамических данных'''
        context = super().get_context_data()
        post = Post.objects.get(slug=self.kwargs['slug'])
        context['comments'] = Comment.objects.filter(post=post)
        context['comment_form'] = CommentForm
        return context


class PostByCategory(BlogListView):
    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['pk'], is_published=True)


def add_comment(request, slug):
    '''Добавление комментария статьи'''
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = Post.objects.get(slug=slug)
        comment.save()
    return redirect('post_detail', slug)


