from django.contrib import admin

from .models import Testimonial, successfulStudent, DynamicContent, EntrySubmission, UcatCourseDetails

# Register your models here.
admin.site.register(Testimonial)
admin.site.register(successfulStudent)
admin.site.register(DynamicContent)
admin.site.register(EntrySubmission)
admin.site.register(UcatCourseDetails)