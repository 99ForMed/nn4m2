from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


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

class EntrySubmission(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    atar = models.DecimalField(max_digits=10, decimal_places=2)
    gpa = models.DecimalField(max_digits=10, decimal_places=2)
    phone = PhoneNumberField(null=True, blank=True, region = 'AU', default=None)
    submitted_datetime = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Entry Submission'
        verbose_name_plural = 'Entry Submissions'
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class UcatCourseDetails(models.Model):

    custom_letter = models.TextField()
    subtext = models.CharField(max_length = 400)
    title = models.CharField(max_length = 400)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    course_start = models.DateField()
    course_end = models.DateField()

    def __str__(self):
        return 'Edit me...'



    class Meta:
        verbose_name = 'UCAT Course'
        verbose_name_plural = 'UCAT Course'
