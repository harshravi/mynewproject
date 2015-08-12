from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

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
