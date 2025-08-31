from .serializers import BlogPostSerializers, ProfileSerializers
from  rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from .models import BlogPost, Profile


class BlogPostView(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    permission_classes = [AllowAny]
    
 
class ProfileView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers


class BlogPostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    permission_classes = [AllowAny]
   