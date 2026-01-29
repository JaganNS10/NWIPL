from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, JobApplication
from .forms import JobApplicationForm
from django.contrib import messages
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


from django.conf import settings
import os


import threading
from django.core.mail import send_mail, EmailMessage


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


def products(request):
    return render(request,'products.html')







# Threaded email sender
def send_email_thread(email_msg):
    try:
        email_msg.send()
    except Exception as e:
        print("Email error:", e)

def job_apply(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            full_name = f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
            job_title = job.title

            application = form.save(commit=False)
            application.job = job
            # application.save()  # Save to DB

            # User confirmation email
            subject_user = "Application Received – Neminath Wood Industry Pvt Ltd"
            message_user = (
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

            # Send confirmation email in a thread
            user_email_msg = EmailMessage(
                subject_user,
                message_user,
                settings.DEFAULT_FROM_EMAIL,
                [form.cleaned_data['email']],
            )
            threading.Thread(target=send_email_thread, args=(user_email_msg,)).start()

            # HR notification email
            resume = request.FILES['resume']
            subject_hr = f"Job Application from {full_name}"
            message_hr = (
                f"{full_name} has applied for {job_title}.\n"
                f"Email: {form.cleaned_data['email']}\n"
                f"Contact: {form.cleaned_data['contact']}\n"
                f"Gender: {form.cleaned_data['gender']}\n"
                f"Year of Graduation: {form.cleaned_data['year_of_graduation']}\n"
                f"Experience: {form.cleaned_data['experience_years']}\n"
                f"Current Employer: {form.cleaned_data['current_employer']}\n"
                f"Notice Period: {form.cleaned_data['notice_period']}\n"
                f"Current CTC: {form.cleaned_data['current_ctc']}\n"
                f"Expected CTC: {form.cleaned_data['expected_ctc']}\n"
                f"Current Location: {form.cleaned_data['current_location']}"
            )

            hr_email_msg = EmailMessage(
                subject_hr,
                message_hr,
                settings.DEFAULT_FROM_EMAIL,
                ['hr@nwipl.com'],
            )
            hr_email_msg.attach(resume.name, resume.read(), resume.content_type)
            threading.Thread(target=send_email_thread, args=(hr_email_msg,)).start()

            messages.success(
                request,
                f'Your application for {job_title} has been submitted successfully. '
                f'Check your email for confirmation.'
            )
            return redirect('careers')
        else:
            print(form.errors)
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    else:
        form = JobApplicationForm()

    return render(request, 'job_apply.html', {'job': job, 'form': form})


def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        name = f"{first_name} {last_name}"
        email = request.POST.get('email')
        message_ = request.POST.get('message')

        subject = "New Enquiry from Website Contact Page"
        message_text = (
            f"You have received a new enquiry through the website contact page.\n\n"
            f"Name: {name}\nEmail: {email}\nMessage: {message_}"
        )

        # Threaded send
        contact_email_msg = EmailMessage(
            subject,
            message_text,
            settings.DEFAULT_FROM_EMAIL,
            ['hr@nwipl.com'],
        )
        threading.Thread(target=send_email_thread, args=(contact_email_msg,)).start()

        messages.success(
            request,
            f"Thank you {name} for contacting Neminath Wood Industry Private Limited. We will contact you shortly!"
        )
        return redirect('Home')

    return redirect('Home')


# def contact(request):
#     if request.method == 'POST':
#         print(request.POST)
#         first_name = request.POST.get('first-name')
#         last_name = request.POST.get('last-name')
#         name = first_name + " " +last_name
#         email = request.POST.get('email')
#         message_ = request.POST.get('message')
#         subject = "New Enquiry from Website Contact Page"
#         message = f"You have received a new enquiry through the website contact page. Please find the details below\nName: {name}\nEmail: {email}\nMessage: {message_}"
#         send_mail(
#             subject,
#             message,
#             from_email='hr@nwipl.com',
#             recipient_list=['hr@nwipl.com']
#         )
#         messages.success(request, f"“Thank you {name} for contacting Neminath Wood Industry Private Limited. We will contact you shortly!”✅")

#         return redirect('Home')
    
#     return redirect('Home')


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
        
#             subject = "Application Received – Neminath Wood Industry Pvt Ltd"

#             message = (
#                 f"Hi {full_name},\n\n"
#                 f"Thank you for your interest in Neminath Wood Industry Private Limited.\n"
#                 f"We have successfully received your application for the position of {job_title}.\n\n"
#                 f"Due to the high number of applications, we will contact only shortlisted "
#                 f"candidates for the next stage of the recruitment process.\n\n"
#                 f"Our team carefully reviews every application, so we appreciate your patience.\n\n"
#                 f"Best regards,\n"
#                 f"Neminath Wood Industry Private Limited\n"
#                 f"Talent Acquisition Team"
#             )

#             send_mail(
#                 subject,
#                 message,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[form.cleaned_data['email']],
#             )


#             email = form.cleaned_data['email']
#             Contact = form.cleaned_data['contact']
#             year_of_graduation = form.cleaned_data['year_of_graduation']
#             gender = form.cleaned_data['gender']
#             experience = form.cleaned_data['experience_years']
#             notice_period = form.cleaned_data['notice_period']
#             current_employer = form.cleaned_data['current_employer']
#             current_ctc = form.cleaned_data['current_ctc']
#             expected_ctc = form.cleaned_data['expected_ctc']
#             current_location = form.cleaned_data['current_location']
#             resume = request.FILES['resume'] 
#             subject = f"Job Application from {full_name}"
#             message = f"{full_name} has applied for a {job_title}.\nEmail: {email}\nContact: {Contact}\ngender: {gender}\nYear of graduation: {year_of_graduation}\nexperience: {experience}\ncurrent employer: {current_employer}\nnotice_period: {notice_period}\nCurrent ctc: {current_ctc}\nExpected ctc: {expected_ctc}\ncurrent location: {current_location}"
#             hr_email = 'hr@nwipl.com'

#             email_msg = EmailMessage(
#                 subject,
#                 message,
#                 'hr@nwipl.com',
#                 [hr_email],                
#             )
#             email_msg.attach(resume.name, resume.read(), resume.content_type)
#             email_msg.send()

#             print("Email sent successfully")
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



