from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, JobApplication
from .forms import JobApplicationForm
from django.contrib import messages


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
            messages.success(request, 'Your application has been submitted successfully.')
            return redirect('careers')
        else:
            print(form.errors)
    else:
        print(False)
        form = JobApplicationForm()

    return render(request, 'job_apply.html', {
        'job': job,
        'form': form
    })


def products(request):
    return render(request,'products.html')




