from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("<h1>This is the about page of my first Django app.</h1>")

def contact(request):
    return render(request, 'contact.html')