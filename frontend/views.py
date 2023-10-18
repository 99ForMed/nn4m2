from django.shortcuts import render, redirect
from .functions import handle_uploaded_file
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .models import Testimonial, successfulStudent

# Create your views here.

def home_view(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials,
        'testimonials_all': testimonials,
        'testimonials_grouped': [testimonials[n:n+3] for n in range(0, len(testimonials), 3)]
    }
    return render(request, 'index.html', context) 

def eligibility_view(request):
    # Validate all the info as well
    
    if request.method == 'POST':
        if 'atar' in request.POST:
            accepted = False
            status_list = ['accepted', 'waiting_to_be_contacted', 'rejected']
            atar = float(request.POST['atar'])
            try:
                gpa = float(request.POST['gpa'])
            except ValueError as e:
                None
            if atar > 96 or gpa > 6:
                accepted = True
                return redirect('secondary-qualifiers/?fname=%s&lname=%s&email=%s&pn=%s&sm=%s&gpa=%s&a=%s&atar=%s' % (request.POST['fname'], request.POST['lname'], request.POST['email'], request.POST['mob'], request.POST['job'], request.POST['gpa'], str(accepted), str(atar)))
            elif atar < 93 and gpa < 5.5:
                return redirect('../rejected/?scores=1')
            else:
                return redirect('secondary-qualifiers/?fname=%s&lname=%s&email=%s&pn=%s&sm=%s&gpa=%s&a=%s&atar=%s' % (request.POST['fname'], request.POST['lname'], request.POST['email'], request.POST['mob'], request.POST['job'], request.POST['gpa'], str(accepted), str(atar)))

    context = {

    }
    return render(request, 'eligibility.html', context)

def secondary_qualifiers_view(request):
    
    if request.method == 'POST':
        if request.GET['a'] == "False":
            accepted = False
        elif request.GET['a'] == "True":
            accepted = True
        else:
            print("Error with the thing. sorry.")

        if float(request.GET['atar']) > 93 and request.POST['gsw'] == 'on':
            print('accepted for gsw consideration')
            accepted = True

        if float(request.POST['hours-amount']) > 90:
            print(int(request.POST['hours-amount']))
            return redirect('../rejected/?hours=1')
        if accepted:
            status = "accepted"
        else:
            status = "waiting"

        if 'gsw' in request.POST.keys():
            gsw = True
        else:
            gsw = False

        files=[]
        for key in request.FILES.keys():
            files.append(request.FILES[key])

        email_package = {
            'author': 'website.notification@yourweb.sydney',
            'recipients': ['admin@yourweb.sydney'],
            'subject': '99ForMed Application - ' + request.GET['fname']+' '+request.GET['lname'],
            'template': 'application-email.html',
            'context': {
                'title: ': "Status: " + status,
                'fname': request.GET['fname'],
                'lname': request.GET['lname'],
                'email': request.GET['email'],
                'pn': request.GET['pn'],
                'sm': request.GET['sm'],
                'atar': request.GET['atar'],
                'gpa': request.GET['gpa'],
                'gsw': gsw,
                'hours': str(int(request.POST['hours-amount'])/10),
                'commitment_explanation': request.POST['commitment-explanation'],
                'study_plan': request.POST['ucat-plan']
                

            },
            'files': files
        }

        html_content = render_to_string('application-email.html', email_package['context'])
        email = EmailMultiAlternatives(
            email_package['subject'],
            'This email is unavailable from this browser. Please contact admin@yourweb.sydney if this is an urgent issue.',
            'website.notification@yourweb.sydney',
            ['pri@yourpulse.com.au', 'info@99formed.com']
        )

        email.attach_alternative(html_content, "text/html")
        for file in files:
            email.attach(file.name, file.file.read(), 'application/pdf')
        email.send()


        if accepted:
            
            return redirect('/eligibility-check/accepted/')
        else:
            return redirect('/eligibility-check/submitted/')
        


    context = {

    }
    return render(request, 'secondary-qualifiers.html', context)


def accepted_view(request):
    context = {

    }
    return render(request, 'accepted.html', context)

def rejected_view(request):
    scores = False
    hours = False

    if 'scores' in request.GET.keys():
        scores = True
    
    if 'hours' in request.GET.keys():
        hours = True
    
    context = {
        'scores': scores,
        'hours': hours
    }
    return render(request, 'rejected.html', context)

def submitted_view(request):
    context = {}
    return render(request, 'submitted.html', context)

def coming_soon_view(request):
    context = {

    }
    return render(request, 'coming-soon.html', context)

def our_story_view(request):
    context = {

    }
    return render(request, 'our-story.html', context)

def courses_view(request):
    context = {

    }
    return render(request, 'courses.html', context)

def ucat_view(request):
    context = {

    }
    return render(request, 'ucat.html', context)

def interview_view(request):
    context = {

    }
    return render(request, 'interview.html', context)

def our_story_view(request):
    context = {

    }
    return render(request, 'our-story.html', context)

def successful_students_view(request):

    render_students = []

    for student in successfulStudent.objects.all():
        render_students.append({
            'logo': student.university,
            'name': student.name,
            'score': student.score,
            'percentile': student.percentile
        })
    

    context = {

        'render_students': render_students

    }
    return render(request, 'successful-students.html', context)

def full_testimonial_view(request, id):
    context = {
        'testimonial': Testimonial.objects.get(id = id)
    }
    return render(request, 'full-testimonial.html', context)

def ucat_course_content_view(request):
    context = {
    }
    return render(request, 'ucat-course-content.html', context)

def medicine_interview_course_content_view(request):
    context = {

    }
    return render(request, 'medicine-interview-course-content.html', context)

def dentistry_interview_course_content_view(request):
    context = {

    }
    return render(request, 'dentistry-interview-course-content.html', context)

def contact_view(request):
    context = {

    }
    return render(request, 'contact.html', context)