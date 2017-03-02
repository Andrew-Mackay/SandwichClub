from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Home page")

def login(request):
	return HttpResponse("Login page")
	
def profile(request):
	return HttpResponse("Profile page")
	
def register(request):
	return HttpResponse("Registration page")
	
def categories(request):
	return HttpResponse("Categories page")
	
def about(request):
	return HttpResponse("About page")