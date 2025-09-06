from django.shortcuts import render
from django.http import HttpResponse
from .models import ChaiVarity

# chai/views.py
# from .models import Product
# from django.utils import timezone



# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, "DjangoApp/index.html", {"chais": chais})


def home(request):
    return render(request, "DjangoApp/e-comerce.html")

def chai_detail(request, chai_id):
    chai = ChaiVarity.objects.get(id=chai_id)
    return render(request, "DjangoApp/chai_detail.html", {"chai": chai})
