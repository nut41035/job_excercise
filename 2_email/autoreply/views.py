from django.shortcuts import render
from django.http import HttpResponse
from .forms import sendForm
from django.core.mail import send_mail
from django.template import loader

def index(request):
#     send_mail(
#         'subject',
#         'message body',
#         'excercise.receiever@gmail.com',
#         ['excercise.sender@gmail.com'],
#         fail_silently=False,
#     )
    template = loader.get_template('autoreply/autoreply.html')
    context = {
        'form' : sendForm
    }
    return HttpResponse(template.render(context, request))

def send(request):
    if request.method == 'POST':
        f = sendForm(request.POST)
        if f.is_valid():
            to = f.cleaned_data['to']
            name = f.cleaned_data['name']
            subject = f.cleaned_data['subject']
            message = f.cleaned_data['message']
            
            body = "Dear K. %s, \n   %s"%(name, message)       
            
            send_mail(
                subject,
                body,
                'excercise.sender@gmail.com',
                [to],
                fail_silently=False,
            )
    return index(request)
# Create your views here.
