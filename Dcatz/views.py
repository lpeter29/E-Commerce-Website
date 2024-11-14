from django.shortcuts import render, loader
from django.http import HttpResponse

def master(request):
    template = loader.get_template('master.html')
    return HttpResponse(template.render())
    
def home_page(request):
    return render(request, 'home-page.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def sign_up(request):
    return render(request, 'sign_up.html')