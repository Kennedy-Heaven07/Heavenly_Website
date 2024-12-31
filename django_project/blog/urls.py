# blog/urls.py
from django.urls import path
from .views import HomePageView,AboutPageView
from . import views  # Import the views module
from .views import signup
from .views import (
BlogListView,
BlogDetailView,
BlogCreateView,
BlogUpdateView,
BlogDeleteView, # new
)
urlpatterns = [
path("", HomePageView.as_view(), name="home"),
path("post/new/", BlogCreateView.as_view(), name="post_new"),
path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
path("post/<int:pk>/edit/", BlogUpdateView.as_view(),
name="post_edit"),
path("post/<int:pk>/delete/", BlogDeleteView.as_view(),
name="post_delete"), # new
path("", BlogListView.as_view(), name="home"),
path("about/", AboutPageView.as_view(), name="about"), # new
 path('mysignup/', signup, name='mysignup'),
]