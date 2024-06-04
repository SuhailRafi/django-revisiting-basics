from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

def about(request):
    return HttpResponse("<h1>Anything about me!</h1>")

def hello (request, first_name):
    return HttpResponse(f"<h1>Hello {first_name}!</h1>")

def add (request, num1, num2):
    return HttpResponse(f"The total is {num1+num2}")

# def greeting(request, name):
#     return HttpResponse(f"<h1>Hello {name.capitalize()}!</h1>")