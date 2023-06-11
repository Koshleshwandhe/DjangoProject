from django.http import HttpResponse
from django.shortcuts import render

# Code for video 7

def index(request):
    return render(request, 'index.html')

def removepunc(request):
    #Get the text
    print(request.GET.get('text','default'))
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")