from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("our new project updated")