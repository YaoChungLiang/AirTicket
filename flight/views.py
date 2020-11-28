from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sample(req):
    return HttpResponse('Let"s travel!')

def get_info(req, age):
    return HttpResponse(f'I am {age} years old!')

def even_odd(req, num):
    output = ''
    if num%2:
        output = f'Input is odd'
    else:
        output = f'Input is even'
    return HttpResponse(output)

