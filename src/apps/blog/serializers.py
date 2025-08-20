from .models import BlogPost
from rest_framework import serializers


class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"