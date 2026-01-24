from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, JobApplication
from .forms import JobApplicationForm
from django.contrib import messages
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from email.mime.image import MIMEImage
import os

def Home(request):
    return render(request,'index.html')


# def Modularkitchen(request):
#     return render(request,'ModularKitchen.html')

def Furnitureforkids(request):
    return render(request,'FurnitureforKids.html')

def Tvunit(request):
    return render(request,'TVUnit.html')

def Wardrobe(request):
    return render(request,'Wardrobe.html')

def ClassicRanges(request):
    return render(request,'ClassicRanges.html')

def SkinRanges(request):
    return render(request,'SkinRanges.html')

def VeneerRanges(request):
    return render(request,'VeneerRanges.html')

def LaminateRanges(request):
    return render(request,'LaminateRanges.html')

def LightOpeningRanges(request):
    return render(request,'LightOpeningRanges.html')

def Corporate(request):
    return render(request,'Corporate.html')

def seasoningchamber(request):
    return render(request,'seasoningchamber.html')

# def careers(request):
#     jobs = Job.objects.filter(is_active=True)
#     return render(request, 'job_list.html', {'jobs': jobs})


def careers(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request,'careers.html',{'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id, is_active=True)
    return render(request, 'job_detail.html', {'job': job})


# def job_apply(request, id):
#     job = get_object_or_404(Job, id=id)

#     if request.method == 'POST':

#         form = JobApplicationForm(request.POST, request.FILES)
#         print(request.POST)
#         if form.is_valid():
#             full_name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
#             job_title = job.title
#             print(True)
#             application = form.save(commit=False)
#             application.job = job
#             # application.save()
#             print(form.cleaned_data)
#             user_email = request.POST.get('email')

#             subject = "Welcome to Neminath Wood Industry Private Limited"

#             html_content = render_to_string("sendemailtoperson.html", {
#                         'full_name': full_name,
#                         'job_title': job_title,
#                         'year': timezone.now().year,
#                     })

#             text_content = strip_tags(html_content)

#             email_msg = EmailMultiAlternatives(
#                         subject,
#                         text_content,
#                         settings.EMAIL_HOST_USER,
#                         [user_email]
#                     )

#             email_msg.attach_alternative(html_content, "text/html")

#             email_msg.send()

#             messages.success(request, f'Your application for the position of {job_title} has been submitted successfully.Check Your mail for more details.Our team will review your application and get back to you soon.thank you for considering a career with Neminath Wood Industry Private Limited.')
#             return redirect('careers')
        
#         else:
#             print(form.errors)
#             messages.error(request, 'There was an error with your submission. Please correct the errors below.')
#     else:
#         print(False)
#         form = JobApplicationForm()


#     return render(request, 'job_apply.html', {
#         'job': job,
#         'form': form
#     })


def job_apply(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == 'POST':

        form = JobApplicationForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
            job_title = job.title
            print(True)
            application = form.save(commit=False)
            application.job = job
            # application.save()
            
            print(form.cleaned_data)
            subject = "Application Received – Neminath Wood Industry Pvt Ltd"

            message = (
                f"Hi {full_name},\n\n"
                f"Thank you for your interest in Neminath Wood Industry Private Limited.\n"
                f"We have successfully received your application for the position of {job_title}.\n\n"
                f"Due to the high number of applications, we will contact only shortlisted "
                f"candidates for the next stage of the recruitment process.\n\n"
                f"Our team carefully reviews every application, so we appreciate your patience.\n\n"
                f"Best regards,\n"
                f"Neminath Wood Industry Private Limited\n"
                f"Talent Acquisition Team"
            )

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
            )
            messages.success(request, f'Your application for the position of {job_title} has been submitted successfully.Check Your mail for more details.Our team will review your application and get back to you soon.thank you for considering a career with Neminath Wood Industry Private Limited.')
            return redirect('careers')
        
        else:
            print(form.errors)
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    else:
        print(False)
        form = JobApplicationForm()


    return render(request, 'job_apply.html', {
        'job': job,
        'form': form
    })


def products(request):
    return render(request,'products.html')










