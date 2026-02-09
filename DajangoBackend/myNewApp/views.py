from django.shortcuts import render

# Create your views here.
def chai_order(request) :
    return render(request,'myNewApp/app_all.html')
