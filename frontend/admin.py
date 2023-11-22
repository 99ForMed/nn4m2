from django.contrib import admin

from .models import Testimonial, successfulStudent, DynamicContent

# Register your models here.
admin.site.register(Testimonial)
admin.site.register(successfulStudent)
admin.site.register(DynamicContent)