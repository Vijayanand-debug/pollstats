from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def getusernumbers(req,event_code):
    print(User)
    return render(req, 'stats.html',{})