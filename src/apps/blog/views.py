from .serializers import BlogPostSerializers
from  rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import BlogPost


class BlogPostView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    

 