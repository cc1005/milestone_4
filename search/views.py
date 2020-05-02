from django.shortcuts import render
from catalogue.models import Catalogue

# Create your views here.

def do_search(request):
    catalogue = Catalogue.objects.filter(name__icontains=request.GET['q'])
    return render(request, "catalogue.html", {"catalogue":catalogue})