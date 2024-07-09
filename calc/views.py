from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()

    return render(request, 'index.html',{'price':700})






