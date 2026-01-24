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


def job_apply(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == 'POST':

        form = JobApplicationForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            print(True)
            application = form.save(commit=False)
            application.job = job
            # application.save()

            name = request.POST.get('name')
            user_email = request.POST.get('email')

            subject = "Welcome to Our Company"

            html_content = render_to_string("sendemailtoperson.html", {
                        'name': name,
                        'year': timezone.now().year,
                    })

            text_content = strip_tags(html_content)

            email_msg = EmailMultiAlternatives(
                        subject,
                        text_content,
                        settings.EMAIL_HOST_USER,
                        [user_email]
                    )

            email_msg.attach_alternative(html_content, "text/html")

            email_msg.send()

            
            messages.success(request, 'Your application has been submitted successfully.')
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




def form_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_email = request.POST.get('email')

        subject = "Welcome to Our Company"

        html_content = render_to_string("contactemail.html", {
            'name': name,
            'year': timezone.now().year,
        })

        text_content = strip_tags(html_content)

        email_msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.EMAIL_HOST_USER,
            [user_email]
        )

        email_msg.attach_alternative(html_content, "text/html")

        # ✅ Correct static path (Render-safe)
        logo_path = os.path.join(settings.STATIC_ROOT, 'assets/images/NeminathLogo.png')

        if os.path.exists(logo_path):
            with open(logo_path, 'rb') as f:
                logo = MIMEImage(f.read())
                logo.add_header('Content-ID', '<companylogo>')
                logo.add_header('Content-Disposition', 'inline', filename="logo.png")
                email_msg.attach(logo)

        email_msg.send()

        return redirect('home')

    return redirect('home')





