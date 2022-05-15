from django.db import models

# Create your models here.
class Message(models.Model):
    msg=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_byId=models.IntegerField()
    username=models.CharField(max_length=50)
    email=models.EmailField()


    def __str__(self):
        return self.msg