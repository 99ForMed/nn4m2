from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    credentials = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name