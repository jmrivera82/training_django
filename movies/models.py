from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    synopsis= models.TextField()

    def __str__(self): 
        return f"{self.id} - {self.title}"
    
    