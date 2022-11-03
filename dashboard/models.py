from django.db import models

# Create your models here.
class BookReview(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    review = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.author}'