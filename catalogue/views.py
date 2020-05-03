from django.shortcuts import render, get_object_or_404, redirect
from .models import Catalogue, FullDocument
from django.contrib.auth import authenticate
from checkout.models import Customer
from checkout.views import checkout

# Create your views here.

def total_catalogue(request):
    catalogue = Catalogue.objects.all()
    return render(request, "catalogue.html", {"catalogue": catalogue})

def access_full_documents(request):
    plan = get_object_or_404(FullDocument)
    if request.user.is_authenticated:
        try:
            if request.user.customer.membership:
                return render(request, 'catalogue/fulldocument.html', {'plan':plan})
        except Customer.DoesNotExist:
            return redirect('join')
    else:
        return redirect('join')