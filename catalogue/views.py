from django.shortcuts import render, get_object_or_404, redirect
from .models import Catalogue, FullDocument
from django.contrib.auth import authenticate
from checkout.models import Customer
from checkout.views import checkout

# Create your views here.

def total_catalogue(request):
    catalogue = Catalogue.objects.all()
    return render(request, "catalogue.html", {"catalogue": catalogue})

def access_full_documents(request, fulldocument_id):
    fulldocument = get_object_or_404(FullDocument, pk=fulldocument_id)
    catalogue = get_object_or_404(Catalogue)
    if request.user.is_authenticated:
        try:
            if request.user:
                customer = Customer.objects.get(user=request.user)
                return render(request, "fulldocument.html", {'fulldocument':fulldocument, 'customer':customer, 'catalogue':catalogue})
        except Customer.DoesNotExist:
            return redirect('registration')
    else:
        return redirect('registration')


