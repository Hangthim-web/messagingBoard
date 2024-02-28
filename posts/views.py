from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from posts.models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html";