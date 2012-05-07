# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from events.models import Event

def home(request):
  data = {}
  return render_to_response("events/home.html", data, context_instance=RequestContext(request))

def configure(request):
  data = {}

  # TODO: Need to track people posting their e-mails and event names
  
  data["topics"] = [{
                      "title": "Round 1 Topic",
                      "questions": ["Technology",
                                    "Health",
                                    "Entrepreneurship",
                                    "Management"]
                    },
                    {
                      "title": "Round 2 Topic",
                      "questions": ["Family",
                                    "Education",
                                    "Elderly Care",
                                    "Community Service",
                                    "Retirement Plans"]
                    },
                    {
                      "title": "Round 3 Topic",
                      "questions": ["Travel",
                                    "Sports",
                                    "TV Shows",
                                    "Ballet",
                                    "Opera",
                                    "Musical",
                                    "Circus"]
                    },
                    {
                      "title": "Round 4 Topic",
                      "questions": ["Healthy Lifestyle",
                                    "Food",
                                    "Dessert",
                                    "Restaurant",
                                    "Fast Food",
                                    "Exercise"]
                    }]


  data["login"] = True
  data["user_email"] = "eventadmin@gmail.com"

  return render_to_response("events/configure.html", data, context_instance=RequestContext(request)) 

def login(request):
  data = {}
  return render_to_response("events/login.html", data, context_instance=RequestContext(request)) 

def logout(request):
  data = {}
  return render_to_response("events/logout.html", data, context_instance=RequestContext(request)) 

def start(request):
  data = {}

  data["login"] = True
  data["user_email"] = "eventadmin@gmail.com"

  return render_to_response("events/start.html", data, context_instance=RequestContext(request)) 

def add_topic(request):
  """

    :param POST['round_id']: round ID
    :param POST['topic']: topic string

  """
  data = {}
  return render_to_response("events/add_topic.html", data, context_instance=RequestContext(request)) 

def del_topic(request):
  """

    :param POST['round_id']: round ID
    :param POST['topic_id']: topic ID 

  """
  data = {}
  return render_to_response("events/del_topic.html", data, context_instance=RequestContext(request)) 

def set_round_duration(request):
  """

    :param POST['duration']: duration in minutes

  """
  data = {}
  return render_to_response("events/set_round_duration.html", data, context_instance=RequestContext(request)) 

def add_user(request):
  """
    :param POST['email']: email
    :param POST['first_name']: first name
    :param POST['last_name']: last name
  """
  data = {}
  return render_to_response("events/add_user.html", data, context_instance=RequestContext(request)) 

def update_user(request):
  """
    :param POST['email']: email
    :param POST['first_name']: first name
    :param POST['last_name']: last name
  """
  data = {}
  return render_to_response("events/update_user.html", data, context_instance=RequestContext(request)) 

def del_user(request):
  """
    :param POST['email']: email (optional)
    :param POST['user_id']: user ID  (optional)
  """
  data = {}
  return render_to_response("events/del_user.html", data, context_instance=RequestContext(request)) 

def survey_completed(request):
  """
    :param POST['email']: email (optional)
  """
  data = {}
  return render_to_response("events/survey_completed.html", data, context_instance=RequestContext(request)) 

def start_round(request):
  """
    :param POST['email']: email 
    :param POST['code']: event code
  """
  data = {}
  return render_to_response("events/start_round.html", data, context_instance=RequestContext(request)) 

def pause_round(request):
  """
    :param POST['email']: email 
    :param POST['code']: event code
  """
  data = {}
  return render_to_response("events/pause_round.html", data, context_instance=RequestContext(request)) 

def end_round(request):
  """
    :param POST['email']: email 
    :param POST['code']: event code
  """
  data = {}
  return render_to_response("events/end_round.html", data, context_instance=RequestContext(request)) 

def restart_round(request):
  """
    :param POST['email']: email 
    :param POST['code']: event code
  """
  data = {}
  return render_to_response("events/restart_round.html", data, context_instance=RequestContext(request)) 

