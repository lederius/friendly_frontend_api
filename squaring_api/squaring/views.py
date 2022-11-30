from django.shortcuts import render
from django.views import View # regular class based view
from django.http import HttpResponse
# Create your views here.

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello World')

class SquaringView(View):
    def get(self, request, number):
        return HttpResponse(number ** 2)