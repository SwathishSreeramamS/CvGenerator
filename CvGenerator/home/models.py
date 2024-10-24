from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=200,)
    email=models.CharField(max_length=200,)
    phone=models.CharField(max_length=200,)
    address=models.TextField(max_length=2000,)
    summary=models.TextField(max_length=2000,)
    degree=models.CharField(max_length=200,)
    pg=models.CharField(max_length=200,)
    school=models.CharField(max_length=200,)
    language=models.CharField(max_length=200,)
    skills=models.TextField(max_length=2000,)
    experience=models.TextField(max_length=2000,)
    
    def __str__(self):
        return self.name