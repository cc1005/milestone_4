from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import PremiumPlan, Customer
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
import stripe
from django.http import HttpResponse

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == 'POST':
        stripe_customer = stripe.Customer.create(email=request.user.email, source=request.POST['stripeToken'])
        plan = 'plan_HCsVwhn77y0sdm'
        if request.POST['plan'] == 'yearly':
            plan = 'plan_HCsWoYCiTPhwd5'
        else:
            subscription = stripe.Subscription.create(customer=stripe_customer.id,
            items=[{'plan':plan}])
        
        customer = Customer()
        customer.user = request.user
        customer.stripeid = stripe_customer.id
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = subscription.id
        customer.save()

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
