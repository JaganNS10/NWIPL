from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, JobApplication
from .forms import JobApplicationForm
from django.contrib import messages
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


from django.core.mail import send_mail
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend
import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.core.mail import EmailMessage


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

def contact(request):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        name = first_name + " " +last_name
        email = request.POST.get('email')
        message_ = request.POST.get('message')
        subject = "New Enquiry from Website Contact Page"
        message = f"You have received a new enquiry through the website contact page. Please find the details below\nName: {name}\nEmail: {email}\nMessage: {message_}"
        send_mail(
            subject,
            message,
            from_email='hr@nwipl.com',
            recipient_list=['hr@nwipl.com']
        )
        messages.success(request, f"“Thank you {name} for contacting Neminath Wood Industry Private Limited. We will contact you shortly!”✅")

        return redirect('Home')
    
    return redirect('Home')


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
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[form.cleaned_data['email']],
            )


            email = form.cleaned_data['email']
            Contact = form.cleaned_data['contact']
            year_of_graduation = form.cleaned_data['year_of_graduation']
            gender = form.cleaned_data['gender']
            experience = form.cleaned_data['experience_years']
            notice_period = form.cleaned_data['notice_period']
            current_employer = form.cleaned_data['current_employer']
            current_ctc = form.cleaned_data['current_ctc']
            expected_ctc = form.cleaned_data['expected_ctc']
            current_location = form.cleaned_data['current_location']
            resume = request.FILES['resume'] 
            subject = f"Job Application from {full_name}"
            message = f"{full_name} has applied for a {job_title}.\nEmail: {email}\nContact: {Contact}\ngender: {gender}\nYear of graduation: {year_of_graduation}\nexperience: {experience}\ncurrent employer: {current_employer}\nnotice_period: {notice_period}\nCurrent ctc: {current_ctc}\nExpected ctc: {expected_ctc}\ncurrent location: {current_location}"
            hr_email = 'hr@nwipl.com'

            email_msg = EmailMessage(
                subject,
                message,
                'hr@nwipl.com',
                [hr_email],                
            )
            email_msg.attach(resume.name, resume.read(), resume.content_type)
            email_msg.send()

            print("Email sent successfully")
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



# def send_resume(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         resume = request.FILES['resume']  # the uploaded file

#         subject = f"Job Application from {name}"
#         message = f"{name} has applied for a job.\nEmail: {email}"

#         hr_email = 'hr@example.com'

#         email_msg = EmailMessage(
#             subject,
#             message,
#             'yourwebsite@example.com',  # sender
#             [hr_email],                # recipient
#         )
#         email_msg.attach(resume.name, resume.read(), resume.content_type)
#         email_msg.send()

# def send_brevo_email(to_email, subject, html_content):
#     """
#     Send email via Brevo (Sendinblue) API
#     """
#     configuration = sib_api_v3_sdk.Configuration()
#     configuration.api_key['api-key'] = os.environ.get('BREVO_API_KEY')  # set this in Render
    
#     api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

#     send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
#         to=[{"email": to_email}],
#         sender={"name": "Neminath Wood Industry Private Limited", "email": "jagan10ns@gmail.com"},  # verified sender
#         subject=subject,
#         html_content=html_content
#     )

#     try:
#         api_response = api_instance.send_transac_email(send_smtp_email)
#         print("Email sent successfully:", api_response)
#     except ApiException as e:
#         print("Exception when sending email:", e)

# def job_apply(request, id):
#     job = get_object_or_404(Job, id=id)

#     if request.method == 'POST':
#         print(os.environ.get('BREVO_API_KEY'))
#         form = JobApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             full_name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
#             job_title = job.title

#             application = form.save(commit=False)
#             application.job = job
#             # application.save()

#             # Prepare email
#             subject = "Application Received – Neminath Wood Industry Pvt Ltd"
#             html_message = f"""
#             <p>Hi {full_name},</p>
#             <p>Thank you for your interest in Neminath Wood Industry Private Limited.</p>
#             <p>We have successfully received your application for the position of <b>{job_title}</b>.</p>
#             <p>Due to the high number of applications, we will contact only shortlisted candidates for the next stage.</p>
#             <p>Best regards,<br>Neminath Wood Industry Pvt Ltd<br>Talent Acquisition Team</p>
#             """

#             # Send email using Brevo API
#             send_brevo_email(form.cleaned_data['email'], subject, html_message)

#             messages.success(
#                 request,
#                 f'Your application for the position of {job_title} has been submitted successfully. '
#                 'Check your email for confirmation. Our team will review your application and get back to you soon.'
#             )
#             return redirect('careers')
#         else:
#             print(form.errors)
#             messages.error(request, 'There was an error with your submission. Please correct the errors below.')
#     else:
#         form = JobApplicationForm()

#     return render(request, 'job_apply.html', {
#         'job': job,
#         'form': form
#     })

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









