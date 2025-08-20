from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key= True,editable= False, default= uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE )
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="profile/", blank= True,null= True)
    def __str__(self):
        return self.name

    
class BlogPost(BaseModel):
    author = models.ForeignKey(Profile, on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images",blank= True, null= True)

    def __str__(self):
        return self.title
    
