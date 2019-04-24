from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request, "pages/home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "pages/contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [123, 2345, 525],
	}
	return render(request, "pages/about.html", my_context)

def courses_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [123, 2345, 525],
	}
	return render(request, "pages/courses.html", my_context)