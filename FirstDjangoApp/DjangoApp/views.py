from django.shortcuts import render
from django.http import HttpResponse

# chai/views.py
# from .models import Product
# from django.utils import timezone



# Create your views here.
def all_chai(request):
    return render(request, "DjangoApp/index.html")


def home(request):
    return render(request, "DjangoApp/e-comerce.html")
