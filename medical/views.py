from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
def index(request):
    return HttpResponseRedirect('/web/home')
def handler404(request):
    response = render_to_response('404.html', {},
    context_instance=RequestContext(request))
    response.status_code = 404
    return response




