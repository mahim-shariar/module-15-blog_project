from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    contect = models.TextField()
    # exta post multiple categorir modde thakte pare akta category er modde multiple post thakte pare
    category = models.ManyToManyField(Category)
    author =models.ForeignKey(Author, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title