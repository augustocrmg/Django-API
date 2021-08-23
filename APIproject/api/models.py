from django.db import models
#from .serializers import ArticleSerializer

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
