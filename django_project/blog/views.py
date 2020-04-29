from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return HttpResponse('<h1>This is blog home page</h1>')

def about(request):
	return HttpResponse('<h1>This is blog about page</h1>')
