# Create your views here.
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from django.urls import reverse_lazy # new
from .models import Post
from django.shortcuts import render
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
class HomePageView(TemplateView):
    template_name = "home.html"
class AboutPageView(TemplateView): # new
    template_name = "about.html"
def signup(request):
    if request.method == 'POST':
        # Handle form submission
        # Retrieve form data, perform validation, create new user, etc.
        pass
    else:
        return render(request, 'mysignup.html')
