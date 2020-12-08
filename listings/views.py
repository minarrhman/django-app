from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import state_choices, bedroom_choices, price_choices


# Create your views here.
def index(Requests):
    listings = Listing.objects.order_by('-list_date', 'price').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = Requests.GET.get('page')
    paged_listings = paginator.get_page(page)
    content = {
        'listings': paged_listings
    }
    return render(Requests, 'listings/listings.html', content)

def listing(Requests, listing_id):
    listing = get_object_or_404(Listing, pk= listing_id)
    content = {
        'listing':listing
    }
    return render(Requests, 'listings/listing.html', content)

def search(Requests):
    query_set = Listing.objects.order_by('-list_date')
    #Search by keywords
    if 'keywords' in Requests.GET:
        keywords = Requests.GET['keywords']
        if keywords:
            query_set = query_set.filter(description__icontains=keywords)
    #Search by City
    if 'city' in Requests.GET:
        city = Requests.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)
    #Search by State

    if 'state' in Requests.GET:
        state = Requests.GET['state']
        if state:
            query_set = query_set.filter(state__iexact=state)
    #Search by bedrooms
    if 'bedrooms' in Requests.GET:
        bedrooms = Requests.GET['bedrooms']
        if bedrooms:
            query_set = query_set.filter(bedrooms__lte=bedrooms)
    #search by price
    if 'price' in Requests.GET:
        price = Requests.GET['price']
        if price:
            query_set = query_set.filter(price__lte=price)

    content = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': query_set,
        'values': Requests.GET
    }

    return render(Requests, 'listings/search.html', content)
