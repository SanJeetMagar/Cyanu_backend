from django.urls import path
from .views import BlogPostView , ProfileView, BlogPostDetailView

urlpatterns = [
    path("", BlogPostView.as_view(), name= "BlogView" ),
    path("<uuid:pk>/",BlogPostDetailView.as_view()),
    path("profileview/", ProfileView.as_view(),name= "profile"),
]
