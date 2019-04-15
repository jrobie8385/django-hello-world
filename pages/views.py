from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def homePageView(request):
    return HttpResponse("Testing this page...")

def newPage(request):
    return HttpResponse("This page helps to test typing in the words 'nextPage/' into the URL after the base server.")

class AnotherPage(TemplateView):
    template_name = "pages/yet_another_page.html"

class RedirectPage(TemplateView):
    template_name = "pages/redirection_page.html"
