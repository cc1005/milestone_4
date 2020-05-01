from django.shortcuts import render

def index(request):
    """This view displays the index page"""
    return render(request, "index.html")