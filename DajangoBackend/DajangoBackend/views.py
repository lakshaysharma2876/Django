from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Welcome to Home page")
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("Welcome to Contact page")

def about(request):
    return HttpResponse("Welcome to About Us page")
