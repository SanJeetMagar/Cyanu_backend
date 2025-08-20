from .serializers import BlogPostSerializers, ProfileSerializers
from  rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import BlogPost, Profile


class BlogPostView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    

 
class ProfileView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers