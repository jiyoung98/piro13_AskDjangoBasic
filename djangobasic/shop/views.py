from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import quote

# Create your views here.

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def view1(request):
    return HttpResponse('Hello, jiyoung')