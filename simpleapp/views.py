from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def home(request):
    amount = 500

    ctx = {
        'amount':amount
    }
    return render(request, 'chapa.html', ctx)

def nextpage(request):
    return render(request, 'next.html')