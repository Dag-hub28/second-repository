from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def orders_home(request):
    return HttpResponse("Orders section is working ✅")
