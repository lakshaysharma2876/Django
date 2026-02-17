from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety

# Create your views here.
def chai_order(request) :
    chais = ChaiVariety.objects.all()
    return render(request,'myNewApp/app_all.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'myNewApp/chai_detail.html', {'chai':chai})
