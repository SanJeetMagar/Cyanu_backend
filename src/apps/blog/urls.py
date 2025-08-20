from django.urls import path
from .views import BlogPostView , ProfileView

urlpatterns = [
    path("blogView/", BlogPostView.as_view(), name= "BlogView" ),
    path("profileview", ProfileView.as_view(),name= "profile"),
]
