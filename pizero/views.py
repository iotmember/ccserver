from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Website

def index(request):
	"""
	View function for home page of site.
	"""

	num_sites = Website.objects.all().count()

	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'num_sites': num_sites},
	)

def demo(request):
	"""
	View function for Demo page
	"""

	hello = "Test page"

	# Render the HTML template p.html with the data in the context variable
	return render(
		request,
		'demo.html',
		context={'hello': hello},
	)
