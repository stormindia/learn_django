from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
# Create your views here.

posts = [
	{
		"author":'abcd',
		"title": 'post-1',
		'content': 'first post',
		'date_posted': date.today()
	},
	{
		"author":'wasd',
		"title": 'post-2',
		'content': 'second post',
		'date_posted': date.today()
	}
]

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})