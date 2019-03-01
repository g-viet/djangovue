from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse

def getNothing(request):
    return HttpResponse("I am nothing")
