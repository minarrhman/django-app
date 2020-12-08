from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices

def index(Requests):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date', 'price')[:3]
    content = {
        'listings':listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(Requests, 'pages/index.html' , content)

def about(Requests):
    realtors = Realtor.objects.order_by('hire_date')
    mvp = Realtor.objects.all().filter(is_mvp=True)
    realtor = {
        'realtors':realtors,
        'mvp':mvp
    }
    return render(Requests, 'pages/about.html',realtor)
