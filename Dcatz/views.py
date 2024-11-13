from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    
