from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse('hello world, you are at onboard index')

# Create your views here.
