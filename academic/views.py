from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'headline' : "Main"}
    return render(request, 'academic/index.html', context)

def papers(request):
    return HttpResponse("This is the papers page.")

def teaching(request):
    return HttpResponse("This is the teaching page.")
