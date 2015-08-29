from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    ''' It serves the index file '''
    return render_to_response("index.html",context_instance = RequestContext(request))

def contact(request):
    ''' It serves the index file '''
    return render_to_response("contact.html",context_instance = RequestContext(request))    

def aboutus(request):
    ''' It serves the index file '''
    return render_to_response("about.html",context_instance = RequestContext(request))  

def faqs(request):
    ''' It serves the index file '''
    return render_to_response("faqs.html",context_instance = RequestContext(request)) 

def benefits(request):
    ''' It serves the index file '''
    return render_to_response("benefits.html",context_instance = RequestContext(request))   

def technology(request):
    ''' It serves the index file '''
    return render_to_response("technology.html",context_instance = RequestContext(request))        

def project(request):
    ''' It serves the index file '''
    return render_to_response("project.html",context_instance = RequestContext(request))       


@csrf_exempt
def send_email(request):
            subject = "Quickerbuild mail"
            name= request.POST.get('name', '')
            email= request.POST.get('email', '')
            msg = request.POST.get('message', '')
            sub = request.POST.get('subject', '')
            message="Name:" + name+ "\n"+ "\n"  +"Email:"+ email + "\n" + "\n" +"Subject: "+sub +"\n" + "\n" +"Message:" +msg;
            if subject and message and email:
                try:
                   send_mail(subject, message, email,['engghrranjan@gmail.com'])
                   return  render_to_response("sendmail.html",RequestContext(request, {'tag': name}))
                except BadHeaderError:
                     return HttpResponse('Invalid header found.')
            else:
            # In reality we'd use a form class
            # to get proper validation errors.
                return HttpResponse('Make sure all fields are entered and valid.')    
