from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
	# Note:"Context must be a dict rather than list." So we have to make dic and fill the posts list in it
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': "About"})
