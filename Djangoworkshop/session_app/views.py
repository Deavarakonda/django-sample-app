from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def set_session (request):
    request.session['username'] = "lehya"
    return HttpResponse("session data set!")
def get_session (request):
    username = request.session.get('username','guest')
    return HttpResponse(f"Hello, {username} !")