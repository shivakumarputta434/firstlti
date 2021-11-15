from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("our new project updated")

def add(request):
    num1=10
    num2=20
    num3=num1+num2
    return HttpResponse("{0} and {1}Total is: {2}".format(num1,num2,num3))