from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required

def home(request):
	# Note:"Context must be a dict rather than list." So we have to make dic and fill the posts list in it
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

@login_required
# Note:basically this decorator adds functionality to an existing function and in this case it adds functionality 
# to our profile view where the user must be logged in to view this page
def about(request):
	return render(request, 'blog/about.html', {'title': "About"})
