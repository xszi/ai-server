from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print(request)
    context = {}
    context["name"] = '666'
    return render(request, "index.html", context)