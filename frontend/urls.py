
from django.urls import path
from .views import home_view, eligibility_view, secondary_qualifiers_view, accepted_view, submitted_view
from .views import coming_soon_view, our_story_view, courses_view, ucat_view, interview_view
from .views import our_story_view, successful_students_view, full_testimonial_view
from .views import ucat_course_content_view, medicine_interview_course_content_view, dentistry_interview_course_content_view, rejected_view

urlpatterns = [
    path('', home_view),
    path('eligibility-check/', eligibility_view),
    path('eligibility-check/secondary-qualifiers/', secondary_qualifiers_view),
    path('eligibility-check/accepted/', accepted_view),
    path('eligibility-check/submitted/', submitted_view),
    path('eligibility-check/rejected/', rejected_view, name='rejected_view'),
    path('coming-soon/', coming_soon_view),
    path('our-story', our_story_view),
    path('courses/', courses_view),
    path('courses/ucat/', ucat_view),
    path('courses/interview/', interview_view),
    path('our-story/', our_story_view),
    path('successful-students/', successful_students_view),
    path('full-testimonial/<str:id>/', full_testimonial_view),
    path('course-content/ucat/', ucat_course_content_view),
    path('course-content/interview/medicine/', medicine_interview_course_content_view),
    path('course-content/interview/dentistry/', dentistry_interview_course_content_view)
    
]
