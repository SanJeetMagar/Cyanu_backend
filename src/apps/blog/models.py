from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key= True,editable= False, default= uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
    

class BlogPost(BaseModel):
    author = models.ForeignKey()
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    