from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == 'POST':
        return redirect('index')
    else:
        plan = 'monthly'
        price = 499
        euro_price = "4.99"
        if request.method == 'GET' and 'plan' in request.GET:
            if request.GET['plan'] == 'yearly':
                plan = 'yearly'
                price = 4900
                euro_price = "49.00"
        return render(request, "checkout.html", {'plan':plan,'price':price,'euro_price':euro_price})
