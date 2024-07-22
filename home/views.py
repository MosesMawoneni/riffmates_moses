from django.http import HttpResponse
from django.shortcuts import render

def credits(request):
    content = "Moses Mawoneni"
    return HttpResponse(content,content_type='text/plain')

def about(request):
    content = "<h1>Our About Page</h1>"
    return HttpResponse(content,content_type='text/html')
