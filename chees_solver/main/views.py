from django.shortcuts import render
from django.http import HttpResponse
from .figure import get_position
from django.http import JsonResponse
def start (request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)


def index (request,figure,fild):

    data={
        "availableMoves":get_position(figure,fild),
        "figure": f"{figure}",
        "currentField": f"{fild}",
        'error':'null'

    }

    print(request,"i wont bi ci",JsonResponse(data).content)
    return JsonResponse(data)

# Create your views here.
