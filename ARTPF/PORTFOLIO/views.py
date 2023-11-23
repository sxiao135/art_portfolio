from django.shortcuts import render
from django.http import HttpResponse
from .models import Works

# Create your views here.
def testing(request):
    return HttpResponse("Hello World!")

def homepage(request):
    return render(request, "portfolio/hpart.html", {
        "works": Works.objects.all()
    })