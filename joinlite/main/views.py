# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def about(request):
  """
    Show how to use T+1
  """
  data = {}

  return render_to_response("main/about.html", data, context_instance=RequestContext(request))

def team(request):
  """
    Show team information
  """
  return render_to_response("main/about.html", data, context_instance=RequestContext(request))

