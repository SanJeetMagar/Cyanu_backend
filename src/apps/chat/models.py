from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class ChatSession(models.Model):
    user = models.ForeignKey(User, null= True, blank= True, on_delete= models.SET_NULL)
    title = models.CharField(max_length= 255, blank=  True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    

# class ChatMessage(models.Model):
#     ROLES_CHOICE  = (
#         ("user", "user"),
#         ("admin", "admin"),
#         ("assistance", "assistance")
#     )
#     session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name= "message")
#     roles = models.CharField(max_length= 20, choices= ROLES_CHOICE)
#     content = models.TextField()
#     token_usage = models.IntegerField(blank=True, null= True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering =["created_at"]

