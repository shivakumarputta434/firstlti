from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("welcome to new project")