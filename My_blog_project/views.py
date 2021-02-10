from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))
