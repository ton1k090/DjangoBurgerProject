from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Product, About, Reviews, BestBurger, Contact, Gallery


class Index(ListView):
    '''Главная страница'''
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'
    extra_context = {'title': 'Главная страница'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['reviews'] = Reviews.objects.all()
        context['best_burgers'] = BestBurger.objects.all()
        context['contacts'] = Contact.objects.all()
        context['galleries'] = Gallery.objects.all()[2:6]
        return context


class AboutView(Index, ListView):
    template_name = 'product/about.html'

    def get_queryset(self):
        return About.objects.all()


class ContactView(TemplateView):
    template_name = 'product/contact.html'
