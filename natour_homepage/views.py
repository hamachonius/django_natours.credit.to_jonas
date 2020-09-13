from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'natour_homepage/homepage.html')

def eggs(request):
    return HttpResponse('huhu')
