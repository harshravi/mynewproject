from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def home(request):
    ''' It serves the index file '''
    return render_to_response("index.html",context_instance = RequestContext(request))