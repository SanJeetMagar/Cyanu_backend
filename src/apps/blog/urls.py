from django.urls import path
from .views import BlogPostView

urlpatterns = [
    path("BlogView/", BlogPostView.as_view(), name= "BlogView" ),
]
