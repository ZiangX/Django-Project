from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Zi',
		'title': 'First blog',
		'content': 'First Blog Post ',
		'date_posted': 'April 29 2020'
	},
	{
		'author': 'Xu',
		'title': 'Second blog',
		'content': 'Swcond Blog Post ',
		'date_posted': 'April 30 2020'
	}
]

def home(request):
	#"Context must be a dict rather than list." So we have to make dic and fill the posts list in it
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': "About"})
