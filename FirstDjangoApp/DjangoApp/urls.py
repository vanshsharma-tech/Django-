from django.urls import path
from . import views

urlpatterns = [
    path('',view.all_chai,name="all_home")
]
