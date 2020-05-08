from django.shortcuts import render, get_object_or_404, redirect
from .models import Catalogue, FullDocument
from django.contrib import messages
from django.contrib.auth import authenticate
from checkout.models import Customer
from checkout.views import checkout

# Create your views here.

def total_catalogue(request):
    catalogue = Catalogue.objects.all()
    return render(request, "catalogue.html", {"catalogue": catalogue})

"""
def access_full_documents(request, catalogue_id):
    fulldocument = get_object_or_404(FullDocument)
    catalogue = get_object_or_404(Catalogue, )
    if request.user.is_authenticated:
        try:
            if request.user:
                customer = Customer.objects.get(user=request.user)
                return render(request, "fulldocument.html", {'fulldocument':fulldocument, 'customer':customer, 'catalogue':catalogue})
        except Customer.DoesNotExist:
            return redirect('registration')
    else:
        return redirect('registration')
"""

def access_full_documents(request, catalogue_id):
    catalogue = get_object_or_404(Catalogue, pk=catalogue_id)
    fulldocument = get_object_or_404(FullDocument, pk=catalogue_id)
    title = catalogue.name
    description = catalogue.description
    fulltext = fulldocument.document_text
    context = {
        "catalogue": catalogue,
        "title": title,
        "description": description,
        "fulltext": fulltext,
    }
    if request.user.is_authenticated:
        try:
            if request.user:
                customer = Customer.objects.get(user=request.user)
                return render(request, "fulldocument.html", context)
        except Customer.DoesNotExist:
            messages.error(request, "You must have premium membership to access this document")
            return redirect('registration')
    else:
        return redirect('registration')

    


