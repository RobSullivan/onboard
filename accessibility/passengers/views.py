from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader



def index(request):

	return render(request, 'passengers/index.html')


def waiting(request):
	return render(request, 'passengers/waiting.html')

def onboard(request):
	return render(request, 'passengers/onboard.html')

def buses(request):
	return HttpResponse('Here is a list of buses on their way.')
