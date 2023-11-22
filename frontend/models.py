from django.db import models

# Create your models here.

UNI_CHOICES =(
    ('empty.png', 'Empty'),
    ("unsw-logo.png", "University of New South Wales"),
    ("wsu-logo.webp", "Western Sydney University"),
    ("griffith-logo.png", "Griffith University"),
    ("une-logo.png", "University of New England"),
    ("charles-stuart-logo.png", "Charles Stuart"),
    ("anu-logo.png", "Australian National University"),
    ("university-of-qld-logo.png", "University of Queensland"),
    ("university-of-adelaide-logo.png", "University of Adelaide"),

    
)

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    credentials = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name

class successfulStudent(models.Model):
    university = models.CharField(max_length = 100, choices = UNI_CHOICES)
    name = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    percentile = models.CharField(max_length=100)
    banner = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

class DynamicContent(models.Model):
    success_rate = models.IntegerField()
    success_amount = models.IntegerField()

    def __str__(self):
        return "Edit me"