from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
