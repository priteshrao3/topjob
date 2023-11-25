from django.shortcuts import render
from .models import Testomonial, Project, ServicePage, Slider
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request): 
    slider = Slider.objects.all()
    services = ServicePage.objects.all()
    project = Project.objects.all()
    testom = Testomonial.objects.all()


    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        send_mail(
            subject,
            name +'\n'+'\n'+   email +'\n'+'\n'+  phone +'\n'+'\n'+ message,
            settings.EMAIL_HOST_USER,
            ['devloperpritesh@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'core/home.html', {'testom':testom, 'project':project, 'services':services, 'slider':slider})



def about(request):
    services = ServicePage.objects.all()
    testom = Testomonial.objects.all()
    return render(request, 'core/about.html', {'services':services, 'testom':testom})


def services(request, servd):
    serv_title = servd.replace('-', ' ')
    service = ServicePage.objects.all()
    services=ServicePage.objects.get(Service_Title=serv_title) 
    return render(request, 'core/service-details.html', {'serv':services, 'services':service})


def contect(request):
    services = ServicePage.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            subject,
            name +'\n'+'\n'+   email +'\n'+'\n'+  subject +'\n'+'\n'+ message,
            settings.EMAIL_HOST_USER,
            ['info@cleanercouch.co.nz'],
            fail_silently=False,
        )
    return render(request, 'core/contact.html',{'services':services})



def termconditions(request):
    services = ServicePage.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        send_mail(
            subject,
            name +'\n'+'\n'+   email +'\n'+'\n'+  phone +'\n'+'\n'+ message,
            settings.EMAIL_HOST_USER,
            ['devloperpritesh@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'core/term-conditions.html',{'services':services})
