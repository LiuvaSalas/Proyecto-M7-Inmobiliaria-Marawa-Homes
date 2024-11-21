from django.shortcuts import redirect, render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
