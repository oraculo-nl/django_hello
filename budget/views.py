from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def transacties(request):
    # return  HttpResponse("Hello")
    return render(request, "budget/transacties.html")