from django.shortcuts import render, get_object_or_404, redirect
from .models import Catalogue, FullDocument
from django.contrib import messages
from django.contrib.auth import authenticate
from checkout.models import Customer
from checkout.views import checkout

# Create your views here.

def total_catalogue(request):
    catalogue = Catalogue.objects.all()
    if request.user.is_authenticated:
        try:
            if request.user:
                customer = Customer.objects.get(user=request.user)
                return render(request, "catalogue.html", {"catalogue": catalogue})
        except Customer.DoesNotExist:
            return render(request, "cataloguejumbotron.html", {"catalogue": catalogue})
    else:
        return render(request, "cataloguejumbotron.html", {"catalogue": catalogue})
    

def access_full_documents(request, catalogue_id):
    cataloguefulldoc = get_object_or_404(Catalogue, pk=catalogue_id)
    fulldocumentfd = Catalogue.objects.get(pk=catalogue_id).fd.all()
    fulldocument = get_object_or_404(fulldocumentfd)
    title = cataloguefulldoc.name
    description = cataloguefulldoc.description
    fulltext = fulldocument.document_text
    context = {
        "cataloguefulldoc": cataloguefulldoc,
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

    


