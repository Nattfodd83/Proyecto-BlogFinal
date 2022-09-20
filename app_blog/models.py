from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=40)
    body = RichTextField()
    author = models.CharField(max_length=40)
    date = models.DateField(default=datetime.now)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'